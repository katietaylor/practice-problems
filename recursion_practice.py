
def reverse_string(word):
    """reverse a string recursively."""
    new_word = ''
    if len(word) == 0:
        return new_word

    new_word += word[-1] + reverse_string(word[:-1])
    return new_word


def reverse_string_simpler(word):
    """reverse a string recursively."""

    if len(word) == 0:
        return ''

    return word[-1] + reverse_string(word[:-1])


def print_evens_in_list(nums):
    if not nums:
        return

    if nums[0] % 2 == 0:
        print nums[0]

    print_evens_in_list(nums[1:])


