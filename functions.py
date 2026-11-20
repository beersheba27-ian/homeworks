from typing import Callable, Sequence
from math import sqrt
from bisect import bisect_left, bisect_right, insort


def get_all_range(numbers: Sequence[int], allowed: range|None = None)->list[int]:
    """
    numbers - sorted list of numbers in ascending order
    allowed - range of numbers (may be empty)
    returns list of numbers that greater or equal minimal value of range and less than maximal value 
    for empty range the function returns the empty list
    for missed second argument the function returns the same "numbers"
    """
    if allowed is None:
        return list(numbers)
    elif allowed.start == allowed.stop:
        return []

    left_idx = bisect_left(numbers, allowed.start)
    right_idx = bisect_right(numbers, allowed.stop - 1)
    return list(numbers[left_idx:right_idx])

def get_all_not_in_range(numbers: Sequence[int], disallowed: range|None = None)->list[int] :
    """
    numbers - sorted list of numbers in ascending order 
    disallowed - range of numbers (may be empty)
    returns list of numbers from "numbers" that are not in a given range
    """
    
    if disallowed is None or disallowed.start == disallowed.stop:
        return list(numbers)
    
    left_idx = bisect_left(numbers, disallowed.start)
    right_idx = bisect_right(numbers, disallowed.stop - 1)
    return list(numbers[:left_idx]) + list(numbers[right_idx:])

def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    "items" is divided on the parts, each of which contains sqrt(len(items)) items
    Each part should be sorted separately by bubble sorting algorithm that you have already implemented
    After that all parts should be merged in one sorted list.
    No limitations for extra space
    Note: To use "sqrt" function from the module "math". This function returns float type
        so you should apply function "int" and the last part may contain more items
    """
    result = []

    items_len = len(items)
    
    if items_len == 0:
        return result
    
    chunk_len = int(sqrt(items_len))
    chunks_count = items_len // chunk_len

    for i in range(0, chunks_count):
        if i != chunks_count-1:
            chunk = bubble_sorted(list(items[i*chunk_len : (i + 1) * chunk_len]), key)
        else:
            chunk = bubble_sorted(list(items[i*chunk_len:]), key)
        if i == 0:
            result.extend(chunk)
        else:
            _insort_chunk(result, chunk, key)

    return result

def _insort_chunk[T, K](result: list[T], chunk: list[T], key:Callable[[T], T|K]|None=None) -> None:
    for x in chunk:
        insort(result, x, key=key) # type: ignore

def bubble_sorted[T, K](items: Sequence[T], key:Callable[[T], T|K]|None=None)->list:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accorgance with key function-converter like standard Python sorting 
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers 
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=                
    """
    result = list(items)

    unsorted = True
    size = len(items)
    while(unsorted):
        size -= 1
        unsorted = bool(_move_max_to_end_by_keys(result, size, key))

    return result

def _move_max_to_end_by_keys[T, K](numbers: list[T], length: int, key:Callable[[T], T|K]|None=None):
    nSwaps: int = 0
    for i in range(length):
        left_key = key(numbers[i]) if key else numbers[i]
        right_key = key(numbers[i+1]) if key else numbers[i+1]
        if left_key > right_key: # type: ignore
            nSwaps += 1
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return nSwaps