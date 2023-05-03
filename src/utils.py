from functools import reduce


def camel_to_snake_case(val: str) -> str:
    """Convert a given string from Camel Case to Snake Case."""
    return reduce(lambda x, y: x + ("_" if y.isupper() else "") + y, val).lower()
