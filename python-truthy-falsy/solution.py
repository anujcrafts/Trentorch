
def classify_number(x: int | float) -> str:
    """Return one of the following strings based on x, checked in this exact order using an if/elif/else chain:
    "negative"     if x < 0
    "zero"         if x == 0
    "small"        if 0 < x <= 10
    "large"        if x > 10
    """
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x <= 10:
        return "small"
    else:
        return "large"

def is_truthy(value) -> bool:
    """Return the truthiness of `value` exactly as Python's own rules would determine it 
    (equivalent to bool(value), but implement the logic explicitly rather than calling bool() directly, 
    handle None, numbers, strings, lists, tuples, dicts, and sets).
    """
    if value is None:
        return False
    if isinstance(value, (int, float, complex)):
        return value != 0
    if isinstance(value, (str, list, tuple, dict, set)):
        return len(value) > 0
    
    # Fallback for other potential container/truthy types
    try:
        return len(value) > 0
    except (TypeError, AttributeError):
        return True


def first_truthy(values: list):
    """Return the first value in `values` that is truthy. If no value in the list is truthy, return None. 
    Do not use Python's built-in `any()`, implement the scan explicitly using is_truthy-style checks.
    """
    for val in values:
        if is_truthy(val):
            return val
    return None
