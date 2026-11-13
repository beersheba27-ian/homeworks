import functions
import unittest_print
numbers = [-2, -10, 12, 3, -22, 6, 21, 5, 4 ]
sorted_numbers = [-22, -10, -2, 3, 4, 5, 6, 12, 21]
sorted_numbers_abs = [-2, 3, 4, 5, 6, -10, 12, 21, -22]
sorted_even_odd = [-22, -10, -2, 4, 6, 12, 21, 5, 3]
strings = ["lmn", "aaaaaaa", "w", "bb", "B", "cc"]
sorted_len_str = ["B", "w", "bb", "cc", "lmn", "aaaaaaa"]
sorted_strings = ["B", "aaaaaaa", "bb", "cc", "lmn", "w"]
part1 = [3, 5, 7, -11 ]
part2 = [ 0, 4, -10, -20 ]
merge_expected = [ 0, 3, 4, 5, 7, -10, -11,-20]

unittest_print.print_test(f"Sort of list {numbers}", sorted_numbers,\
                           functions.bubble_sorted, items=numbers)
unittest_print.print_test(f"Sort of list {numbers} according to abs values", sorted_numbers_abs,\
                           functions.bubble_sorted, items=numbers, key=abs) 
unittest_print.print_test(f"Sort of list {strings} ",sorted_len_str ,\
                           functions.bubble_sorted, items=strings, key=lambda s: (len(str(s)), s)) 
unittest_print.print_test(
    "Sort an empty list",
    [],
    functions.bubble_sorted,
    items=[],
)
unittest_print.print_test(
    "Sort a single-element list",
    [42],
    functions.bubble_sorted,
    items=[42],
)
unittest_print.print_test(
    "Sort a list with duplicates and negative values",
    [-3, -1, 0, 2, 2],
    functions.bubble_sorted,
    items=[2, -1, 2, 0, -3],
)
unittest_print.print_test(
    "Sort an already sorted list",
    [1, 2, 3, 4],
    functions.bubble_sorted,
    items=[1, 2, 3, 4],
)
unittest_print.print_test(
    "Sort strings by length",
    ["x", "aa", "bbb"],
    functions.bubble_sorted,
    items=["bbb", "x", "aa"],
    key=len,
)
unittest_print.print_test(
    "Sorting incomparable values raises TypeError",
    "TypeError",
    functions.bubble_sorted,
    items=[1, "two"],
)
unittest_print.print_test(
    "Sorting incomparable key results raises TypeError",
    "TypeError",
    functions.bubble_sorted,
    items=[1, 2],
    key=lambda item: item if item == 1 else "two",
)
print()

unittest_print.print_test(f"Sort of list {numbers} according to even first in Asc, odd after even in Desc",sorted_even_odd ,\
                           functions.even_asc_odd_desc, numbers=numbers )
unittest_print.print_test(
    "Sort an empty list by parity",
    [],
    functions.even_asc_odd_desc,
    numbers=[],
)
unittest_print.print_test(
    "Sort only even numbers ascending",
    [-8, -2, 0, 6],
    functions.even_asc_odd_desc,
    numbers=[0, -2, 6, -8],
)
unittest_print.print_test(
    "Sort only odd numbers descending",
    [9, 5, -3, -7],
    functions.even_asc_odd_desc,
    numbers=[5, -3, 9, -7],
)
unittest_print.print_test(
    "Non-integer values raise TypeError in parity sort",
    "TypeError",
    functions.even_asc_odd_desc,
    numbers=["not an integer"],
)
print()

unittest_print.print_test(f"merge of two parts {part1} and {part2} according to abs values",\
                          merge_expected, functions.merge, part1=part1, part2=part2, key=abs )
unittest_print.print_test(
    "Merge with an empty first sequence",
    [1, 2, 3],
    functions.merge,
    part1=[],
    part2=[1, 2, 3],
)
unittest_print.print_test(
    "Merge with an empty second sequence",
    [1, 2, 3],
    functions.merge,
    part1=[1, 2, 3],
    part2=[],
)
unittest_print.print_test(
    "Merge two empty sequences",
    [],
    functions.merge,
    part1=[],
    part2=[],
)
unittest_print.print_test(
    "Merge uneven sequences with duplicates",
    [1, 2, 2, 4, 8],
    functions.merge,
    part1=[1, 2, 4, 8],
    part2=[2],
)
unittest_print.print_test(
    "Merge by key while preserving left-side order for equal keys",
    [(1, "left"), (1, "right"), (2, "right"), (3, "left")],
    functions.merge,
    part1=[(1, "left"), (3, "left")],
    part2=[(1, "right"), (2, "right")],
    key=lambda item: item[0],
)
unittest_print.print_test(
    "Merging incomparable values raises TypeError",
    "TypeError",
    functions.merge,
    part1=[1],
    part2=["two"],
)
unittest_print.print_test(
    "Merging incomparable key results raises TypeError",
    "TypeError",
    functions.merge,
    part1=[1],
    part2=[2],
    key=lambda item: item if item == 1 else "two",
)
print()

unittest_print.print_results()