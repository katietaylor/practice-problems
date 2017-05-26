terrain1 = [['l', 'l', 'l', 'l'],
            ['l', 'w', 'w', 'l'],
            ['l', 'w', 'w', 'l'],
            ['l', 'l', 'l', 'l']]

terrain2 = [['l', 'l', 'l', 'l', 'l', 'l'],
            ['l', 'l', 'w', 'w', 'l', 'l'],
            ['l', 'l', 'w', 'l', 'w', 'l'],
            ['w', 'w', 'w', 'w', 'l', 'l'],
            ['l', 'l', 'l', 'l', 'l', 'l']]


def is_lake(terrain, y, x):

    if terrain[y][x] == 'l':
        return True

    if y == 0 or x == 0 or x == len(terrain[0]) - 1 or y == len(terrain) - 1:
        return False

    if not is_lake(terrain, y + 1, x):
        return False
    if not is_lake(terrain, y - 1, x):
        return False
    if not is_lake(terrain, y, x + 1):
        return False
    if not is_lake(terrain, y, x - 1):
        return False

    return True


def is_lake2(y, x, terrain, seen=None):

    if not seen:
        seen = set()
        coord = (x, y)
        seen.add(coord)

    if y == 0 or x == 0 or x == len(terrain[0]) - 1 or y == len(terrain) - 1:
        return False

    to_check = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for c in to_check:
        if c in seen:
            continue
        else:
            seen.add(c)

            if terrain[c[1]][c[0]] == 'l':
                continue
            else:
                if not is_lake2(c[1], c[0], terrain, seen):
                    return False
