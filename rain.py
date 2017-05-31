"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""


def rain(buildings):
    """How much rain is trapped in Codelandia?"""
    total_rain = 0
    left_max = 0
    right_max = 0
    prev = None
    current_puddle = 0
    puddle_length = 0
    i = 0

    for building in buildings:

        # handles first value and tallest buildings
        if building >= left_max:
            left_max = building
            right_max = 0
            puddle_length = 0
            total_rain += current_puddle
            current_puddle = 0

        elif building < prev:
            current_puddle += left_max - building
            puddle_length += 1

        elif building > prev:
            current_puddle += left_max - building
            puddle_length += 1
            right_max = building

        elif building < right_max:
            current_puddle -= (left_max - right_max) * (puddle_length - 1)
            total_rain += current_puddle
            left_max = building
            puddle_length = 0
            right_max = 0

        if i == len(buildings) - 1:
            if building < prev:
                break
            elif building >= right_max:
                total_rain += current_puddle

        prev = building
        i += 1

    return total_rain

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
