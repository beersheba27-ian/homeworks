from functions import merge_in_place
from unittest_print import print_test, print_results
numbers_abs = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80,-4, 8 ]
numbers = [-11, 3, 5, 7, -20, -10, 0, 4, 100, -80,-4, 8]
numbers_act = numbers.copy()

numbers_abs_exp = [0, 3, 4, 5, 7, -10, -11, -20, 100, -80,-4, 8]
numbers_exp = [-20, -11, -10, 0, 3, 4, 5, 7, 100, -80,-4, 8]
numbers_abs_act = numbers_abs.copy()
merge_in_place(numbers_act, start=0, len1=4, size=8)
merge_in_place(numbers_abs_act, start=0, len1=4, size=8, key=abs)

print_test(f"merge subparts of the first 8 numbers in the list {numbers} ", numbers_exp,\
                           numbers_act )
print_test(f"merge subparts of the first 8 numbers in the list {numbers_abs} according to the abs values ", numbers_abs_exp,\
                           numbers_abs_act )

# Empty range and empty input
empty_items_expected = []
empty_items = []
merge_in_place(empty_items, start=0, len1=0, size=0)
empty_items_actual = empty_items
print_test("merge an empty list", empty_items_expected, empty_items_actual)

untouched_items_expected = [8, 9]
untouched_items = [8, 9]
merge_in_place(untouched_items, start=1, len1=0, size=0)
untouched_items_actual = untouched_items
print_test("merge an empty range inside a list", untouched_items_expected, untouched_items_actual)

# One side empty, or a range containing only one element
first_empty_expected = [0, 1, 3, 5, 9]
first_empty = [0, 1, 3, 5, 9]
merge_in_place(first_empty, start=1, len1=0, size=3)
first_empty_actual = first_empty
print_test("merge with an empty first subpart", first_empty_expected, first_empty_actual)

second_empty_expected = [0, 1, 3, 5, 9]
second_empty = [0, 1, 3, 5, 9]
merge_in_place(second_empty, start=1, len1=3, size=3)
second_empty_actual = second_empty
print_test("merge with an empty second subpart", second_empty_expected, second_empty_actual)

one_element_expected = [99, 4, 88]
one_element = [99, 4, 88]
merge_in_place(one_element, start=1, len1=1, size=1)
one_element_actual = one_element
print_test("merge a one-element range", one_element_expected, one_element_actual)

# Already ordered, interleaved, and duplicate-value cases
already_merged_expected = [99, 1, 2, 3, 4, 88]
already_merged = [99, 1, 2, 3, 4, 88]
merge_in_place(already_merged, start=1, len1=2, size=4)
already_merged_actual = already_merged
print_test(
    "merge already ordered subparts without changing surrounding items",
    already_merged_expected,
    already_merged_actual,
)

interleaved_expected = [0, 1, 2, 3, 4, 5, 6, 9]
interleaved = [0, 1, 3, 5, 2, 4, 6, 9]
merge_in_place(interleaved, start=1, len1=3, size=6)
interleaved_actual = interleaved
print_test(
    "merge interleaved subparts with surrounding items",
    interleaved_expected,
    interleaved_actual,
)

duplicates_expected = [1, 2, 2, 2, 2]
duplicates = [1, 2, 2, 2, 2]
merge_in_place(duplicates, start=0, len1=2, size=4)
duplicates_actual = duplicates
print_test("merge subparts containing duplicate values", duplicates_expected, duplicates_actual)

# Equal keys preserve the original order between the two subparts.
records_expected = [
    (1, "left-1"),
    (1, "right-1"),
    (2, "right-2"),
    (3, "left-3"),
]
records = [(1, "left-1"), (3, "left-3"),
           (1, "right-1"), (2, "right-2")]
merge_in_place(records, start=0, len1=2, size=4, key=lambda record: record[0])
records_actual = records
print_test("merge by key with equal keys", records_expected, records_actual)


print_results()