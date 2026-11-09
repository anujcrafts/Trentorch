def countdown_with_skip(start: int) -> list:
    """Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    l = []
    current = start
    while current >= 1:
        if current == 3:
            current -= 1
            continue
        l.append(current)
        current -= 1
    return l


def find_first_negative(numbers: list) -> int | None:
    """Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause
    to return None after the loop completes normally.
    """
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            return numbers[i]
        i += 1
    else:
        return None


def sum_with_index(numbers: list) -> dict:
    """Using a for loop with enumerate(), build and return a
    dictionary mapping each index to its cumulative running total.
    """
    result = {}
    current_sum = 0
    for index, value in enumerate(numbers):
        current_sum += value
        result[index] = current_sum
    return result


def manual_iteration_trace(numbers: list) -> list:
    """Replicate by hand what a for loop does internally using iter() and next().
    """
    iterator = iter(numbers)
    result = []
    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break
    return result
