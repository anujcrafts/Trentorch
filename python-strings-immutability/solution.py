def replace_char_at(s: str, index: int, ch: str) -> str:
    """Return a new string equal to `s` with the character at position `index` replaced by `ch`. 
    `index` may be negative. `ch` may be any string, not necessarily one character long. 
    If `index` is out of range (index >= len(s) or index < -len(s)), return `s` unchanged.
    """
    if index >= len(s) or index < -len(s):
        return s
    
    # Handle negative indexing for the slice
    if index < 0:
        actual_index = len(s) + index
    else:
        actual_index = index
        
    return s[:actual_index] + ch + s[actual_index + 1:]


def insert_at(s: str, index: int, text: str) -> str:
    """Return a new string with `text` inserted before position `index`. 
    Slice semantics apply: an `index` at or beyond len(s) appends, and a negative 
    `index` counts from the end (clamped at the start of the string).
    """
    if index < -len(s):
        index = 0
    elif index < 0:
        index = len(s) + index
    elif index > len(s):
        index = len(s)
        
    return s[:index] + text + s[index:]


def join_with_separator(parts: list, sep: str) -> str:
    """`parts` is a list of strings. Build and return one string with `sep` between elements."""
    if not parts:
        return ""
    
    result = parts[0]
    for part in parts[1:]:
        result += sep + part
    return result


def repeat_text(s: str, n: int) -> str:
    """Return `s` repeated `n` times using the * operator."""
    if n <= 0:
        return ""
    return s * n


def total_chars_copied(n: int, piece_length: int) -> int:
    """Model of repeated concatenation copying overhead."""
    if n <= 0:
        return 0
    total_steps_sum = (n * (n + 1)) // 2
    return piece_length * total_steps_sum
