from typing import Callable

def merge_in_place[T, K](items: list[T], start: int, len1: int, size: int ,\
                       key: Callable[[T], K]|None=None)->None:
    """
    merges two sorted by key subparts in place of a list's part
    Time complexity O[N]
    Space complexity O[1] no additional list is created
    items - list of T objects (T any type generic at call time)
    start - start index of a being merged list
    len1 - length of the first subpart
    size - length of whole part
    Example: items - [3, 5, 7, -11, 0, 4, -10, -20, 100, -80,-4, 8 ], key - abs function
    start - 0; len1 - 4; size - 8
    call as  merge_in_place(items, start=0, len1=4, size=8, key=abs)
    updated itesms should be as [0, 3, 4, 5, 7, -10, -11, -20, 100, -80,-4, 8]
    """

    i1 = start
    i2 = start + len1
    mid = i2
    end = start + size

    result = []

    while i1 < mid and i2 < end:
        if key:
            left = key(items[i1])
            right = key(items[i2])
        else:
            left = items[i1]
            right = items[i2]

        if left > right:  # type: ignore
            result.append(items[i2])
            i2 += 1
        else:
            result.append(items[i1])
            i1 += 1

    result.extend(items[i2:end])
    result.extend(items[i1:mid])

    items[start:end] = result
            
   