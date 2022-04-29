def a_contains_b(a, b):
    if not a:
        raise AttributeError("A should not be empty or Null")
    if not b:
        raise AttributeError("B should not be empty or Null")
    a_chars = list(a)
    for char in list(b):
        if char in a_chars:
            a_chars.pop(a_chars.index(char))
        else:
            return False
    return True
