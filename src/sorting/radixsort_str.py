from typing import Callable
from src.sorting.utils.util import itself

from src.sorting.countingsort import key_low_case
from src.sorting.mergesort import m_sort_bu


def rad_sort_str(arr: list, key: Callable = itself, reverse: bool = False):
    """Radix Sort Implementation for strings.

    Args:
        arr: List to sort.
        key: Key function to customize the sort order/extract the string to be used to sort.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    if n <= 1:
        return arr

    # sort them into buckets of length
    # shortest->longest when not reverse
    # longest->shortest when reverse
    m_sort_bum_sort_bu(arr, key=len, reverse=reverse)
    max_len = len(arr[-1]) if not reverse else len(arr[0])

    # LSD radix sort(right to left).
    for str_idx in reversed(range(max_len)):
        get_char_key = lambda s: key_low_case(s[str_idx])
        _cnt_sort_radix(arr, 0, n, max_key=25, key_count_arr=get_char_key, key=key, reverse=reverse)
    return arr


def _cnt_sort_radix(
        arr: list,
        lo: int,
        hi: int,
        *,
        max_key: int,
        key_count_arr: Callable = itself,
        key: Callable = itself,
        reverse: bool = False
):
    """Efficient Counting Sort for radix sort str.

    Prerequisite: Elements in array must be sorted in ascending order by length.
    Note: Just a slightly modified normal counting sort.
    Actually also functions as a normal counting sort.
    """
    m = max_key + 1
    count_arr = [0] * m
    for i in range(m):
        count_arr[i] = []

    # populate starting from the longest string, once entered another bucket, finish.
    seq = reversed(range(lo, hi)) if not reverse else range(lo, hi)
    for i in seq:
        elem = key(arr[i])
        try:
            # key_count_arr will raise IndexError if the string is shorter than the current index
            count_arr[key_count_arr(elem)].append(arr[i])
        except IndexError:
            break

    # repopulate arr in the same direction
    idx = hi - 1 if not reverse else lo
    # start from the end of the array as we are adding items from the back
    sequence = reversed(range(m)) if not reverse else range(m)
    for i in sequence:
        # count arr is FIFO, so the stability is preserved (still the same as normal)
        for j in range(len(count_arr[i])):
            arr[idx] = count_arr[i][j]
            if not reverse:
                idx -= 1
            else:
                idx += 1
    return arr


"""
stable sort

Time Complexity:
    Worst = Best: O(K) where K is the total number of characters in the array.

Space Complexity:
    O(m + n) = O(26 + n) = O(n)
"""
