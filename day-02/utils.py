def safe(levels):
    if len(levels) == 1:
        return True

    if levels[0] == levels[1]:
        return False

    increasing = levels[0] < levels[1]
    last = levels[0]

    for level in levels[1:]:
        diff = abs(last - level)
        if 0 < diff < 4 and (last < level) == increasing:
            last = level
        else:
            return False

    return True
