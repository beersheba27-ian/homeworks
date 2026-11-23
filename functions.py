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
    
    direction = 1 if allowed.step > 0 else -1
    start = allowed.start
    stop = allowed.stop - allowed.step

    if direction*start >= direction*stop:
        return []
    
    if direction < 0:
        start, stop = stop, start

    left_idx = bisect_left(numbers, start)
    right_idx = bisect_right(numbers, stop)
    return list(numbers[left_idx:right_idx])

def get_all_not_in_range(numbers: Sequence[int], disallowed: range|None = None)->list[int] :
    """
    numbers - sorted list of numbers in ascending order 
    disallowed - range of numbers (may be empty)
    returns list of numbers from "numbers" that are not in a given range
    """
    return [x for x in numbers if x not in disallowed] if disallowed else list(numbers)

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
            result = merge(result, chunk, key)

    return result

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

def merge[T, K](part1: Sequence[T], part2: Sequence[T], key: Callable[[T], T|K]|None = None)->list:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """  
    result = []
    len1 = len(part1)
    len2 = len(part2)
    i1 = 0
    i2 = 0

    while i1 < len1 and i2 < len2:
        left_key = key(part1[i1]) if key else part1[i1]
        right_key = key(part2[i2]) if key else part2[i2]
        if left_key > right_key:  # type: ignore
            result.append(part2[i2])
            i2 += 1
        else:
            result.append(part1[i1])
            i1 += 1

    result.extend(part2[i2:])
    result.extend(part1[i1:])

    return result