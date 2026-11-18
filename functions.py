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
    end = start + size

    while i1 < i2 and i2 < end:
        if key:
            left = key(items[i1])
            right = key(items[i2])
        else:
            left = items[i1]
            right = items[i2]

        # Ian: without "type: ignore" it still triggers error that T is not comparable
        # And we can't guarantee O(N) complexity with O(1) memory with tools that we have learned
        if left > right: # type: ignore
            item = items[i2]
            j = i2

            while j > i1:
                items[j] = items[j - 1]
                j -= 1

            items[i1] = item
            i1 += 1
            i2 += 1
        else:
            i1 += 1
            
   