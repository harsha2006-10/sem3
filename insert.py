def insert_at(arr: List[Any], index: int, value: Any) -> List[Any]:
    """Insert value into list `arr` at position `index`.

    Raises IndexError for invalid index. Returns the same list (mutated).
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    if index < 0 or index > len(arr):
        raise IndexError("index out of range")
    arr.insert(index, value)
    return arr
