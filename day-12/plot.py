import sys
import numpy as np


class Region:
    def __init__(self, symbol, nrows, ncols):
        self.symbol = symbol
        self.nrows = nrows
        self.ncols = ncols
        self.sites = set()

    def __contains__(self, site):
        return site in self.sites

    def __str__(self):
        result = []
        for row in range(self.nrows):
            symbols = []
            for col in range(self.ncols):
                symbols.append(self.symbol if (row, col) in self.sites else ".")
            result.append("".join(symbols))
        return "\n".join(result)

    def add(self, site):
        self.sites.add(site)

    def area(self):
        return len(self.sites)

    def perimeter(self):
        p = 0
        for row, col in self.sites:
            for rinc, cinc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r = row + rinc
                c = col + cinc
                if 0 <= r < self.nrows and 0 <= c < self.ncols:
                    p += (r, c) not in self.sites
                else:
                    p += 1
        return p

    def price(self):
        return self.area() * self.perimeter()


class Plot:
    def __init__(self):
        self.symbols = np.array([tuple(line.strip()) for line in sys.stdin.readlines()])
        self.nrows, self.ncols = self.symbols.shape
        self.regions = []

    def neighbors(self, site):
        row, col = site
        for rinc, cinc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r = row + rinc
            c = col + cinc
            if 0 <= r < self.nrows and 0 <= c < self.ncols:
                yield r, c

    def expand_region(self, site):
        symbol = self.symbols[site]
        to_consider = {site}
        region = Region(symbol, self.nrows, self.ncols)

        while to_consider:
            this_site = to_consider.pop()
            assert self.symbols[this_site] == symbol
            assert this_site not in region
            region.add(this_site)
            for neighbor in self.neighbors(this_site):
                if self.symbols[neighbor] == symbol and neighbor not in region:
                    to_consider.add(neighbor)

        return region

    def find_regions(self):
        sites = set((r, c) for r in range(self.nrows) for c in range(self.ncols))
        included = set()

        while unconsidered := sites - included:
            site = unconsidered.pop()
            region = self.expand_region(site)
            self.regions.append(region)
            included.update(region.sites)

    def price(self):
        self.find_regions()
        return sum(region.price() for region in self.regions)
