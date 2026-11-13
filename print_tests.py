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

unittest_print.print_test(f"Sort of list {numbers} according to even first in Asc, odd after even in Desc",sorted_even_odd ,\
                           functions.even_asc_odd_desc, numbers=numbers )

unittest_print.print_test(f"merge of two parts {part1} and {part2} according to abs values",\
                          merge_expected, functions.merge, part1=part1, part2=part2, key=abs )

unittest_print.print_results()