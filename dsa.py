def insert_at(lst, index, value):
    """Insert a value at a given index."""
    if 0 <= index <= len(lst):
        lst.insert(index, value)
    else:
        print("Index out of range")

def delete_at(lst, index):
    """Delete element by index and return the removed value."""
    if 0 <= index < len(lst):
        return lst.pop(index)
    else:
        print("Index out of range")
        return None

def delete_value(lst, value):
    """Delete first occurrence of value, return True if deleted."""
    if value in lst:
        lst.remove(value)
        return True
    else:
        return False

def sort_array(lst, ascending=True, method='builtin'):
    """Sort the array with either builtin or selection sort."""
    if method == 'builtin':
        return sorted(lst, reverse=not ascending)
    elif method == 'selection':
        lst_copy = lst.copy()
        n = len(lst_copy)
        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if ascending:
                    if lst_copy[j] < lst_copy[idx]:
                        idx = j
                else:
                    if lst_copy[j] > lst_copy[idx]:
                        idx = j
            lst_copy[i], lst_copy[idx] = lst_copy[idx], lst_copy[i]
        return lst_copy
    else:
        print("Unknown sorting method")
        return lst


if __name__ == "__main__":
    # Take list input from the user, splitting by space
    data = list(map(int, input("Enter integers separated by space for: ").split()))
    print("original:", data)

    # insert demo
    insert_at(data, 2, 99)
    print("after insert 99 at index 2:", data)

    # delete by index
    removed = delete_at(data, 3)
    print(f"removed element at index 3: {removed} ->", data)

    # delete by value
    ok = delete_value(data, 4)
    print(f"deleted value 4? {ok} ->", data)

    # sorting demo
    data2 = list(map(int, input("Enter integers separated by space for sorting demo: ").split()))
    print("data2 original:", data2)
    print("sorted (builtin ascending):", sort_array(data2, ascending=True, method='builtin'))
    print("sorted (builtin descending):", sort_array(data2, ascending=False, method='builtin'))

    # selection sort demo
    print("sorted (selection ascending):", sort_array(data2, ascending=True, method='selection'))
    print("sorted (selection descending):", sort_array(data2, ascending=False, method='selection'))
