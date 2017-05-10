

def find_largest_sequence(nums):
    """Given a list on nums, what is the largest consecutive sum

    For example:

    >>> find_largest_sequence([1, 2, 6, -1, 11, 3])
    22

    >>> find_largest_sequence([1, 2, 6, -10, -1, 11])
    11

    >>> find_largest_sequence([1, 2, 6, -10, -1, 1])
    9

    >>> find_largest_sequence([-1, -2, -6, -10])
    -1

    >>> find_largest_sequence([2,0,-3,-5,-11,6,4,-1,-12,10])
    10

    >>> find_largest_sequence([2,0,3,5,-11,6,4,-1,-12,10])
    10

    >>> find_largest_sequence([-1,-33,-20,-1000])
    -1

    >>> find_largest_sequence([])
    0

    >>> find_largest_sequence([0,0,0])
    0

    >>> find_largest_sequence([1,2,3,-10,4,5])
    9

    >>> find_largest_sequence([1,2,3,4,5,-10])
    15


    """

    if not nums:
        return 0

    largest = max(nums)
    i = 0

    current_total = 0

    while i < len(nums):

        current_total = max(current_total + nums[i], 0)

        if current_total > largest and current_total > 0:
            largest = current_total

        i += 1

    return largest


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WOOT! ***\n"
