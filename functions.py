from typing import Callable, Sequence

# Ian: I decided to simplify types definition of function arguments not to trigger errors
# that object not supports comparison. It could be solved with custom Protocol and overloads
# for more precise typing, but I think it's way too early
def bubble_sorted(items: Sequence, key: Callable|None = None)->list:
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
    keys = result.copy() if key is None else [key(item) for item in result]

    unsorted = True
    size = len(items)
    while(unsorted):
        size -= 1
        unsorted = bool(_move_max_to_end_by_keys(result, keys, size))

    return result

def _move_max_to_end_by_keys(numbers: list, keys: list, length: int):
    nSwaps: int = 0
    for i in range(length):
        if keys[i] > keys[i + 1]:
            nSwaps += 1
            keys[i], keys[i + 1] = keys[i + 1], keys[i]
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return nSwaps

def even_asc_odd_desc(numbers: list[int])->list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    result = list[int]()
    odds = list[int]()

    for x in numbers:
        if x % 2 == 0:
            result.append(x)
        else:
            odds.append(x)

    result.sort()
    odds.sort(reverse=True)

    result.extend(odds)

    return result

def merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """  
   