from typing import Callable, Sequence
from bisect import insort

def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
      (no additional sorting is required)
    2. Merge of all parts from the created above list  
     
    """
    buffer = list(items)
    result = []

    if key is None:
      key = lambda a: a

    while len(buffer) > 0:
        end = _get_sorted_interval_end(buffer, key=key)
        result = _merge(result, buffer[:end], key=key)
        buffer = buffer[end:]

    return result


def _get_sorted_interval_end[T,K](items: Sequence[T], /,*, key:Callable[[T], T|K]|None=None) -> int:
    i = 0
    length = len(items)

    if key is None:
      key = lambda a: a

    while i < length-1 and key(items[i]) <= key(items[i+1]): # type: ignore
        i += 1

    return i+1

def _merge[T, K](part1: Sequence[T], part2: Sequence[T], key: Callable[[T], T|K]|None = None)->list:
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