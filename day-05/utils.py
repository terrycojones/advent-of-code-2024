import sys


def readData():
    rules = []
    inputs = []
    for line in sys.stdin:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            inputs.append(tuple(map(int, line.split(","))))

    return rules, inputs


def valid(pages, rules, seen):
    try:
        this = pages[0]
    except IndexError:
        return True
    else:
        for first, second in rules:
            if this == first:
                if second in seen:
                    return False
            seen.add(this)
        return valid(pages[1:], rules, seen)
