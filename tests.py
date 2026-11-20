import unittest
from functions import *

class TestGetAllRange(unittest.TestCase):
    def test_default_range(self):
        numbers = [-5, -1, 0, 3, 8]
        self.assertEqual(get_all_range(numbers), numbers)

    def test_select_range(self):
        self.assertEqual(
            get_all_range([-5, -1, 0, 3, 8], range(-1, 8)),
            [-1, 0, 3],
        )

    def test_empty_range(self):
        self.assertEqual(get_all_range([1, 2, 3], range(4, 4)), [])

    def test_no_matches(self):
        self.assertEqual(get_all_range([1, 2, 3], range(5, 8)), [])

    def test_empty_numbers(self):
        self.assertEqual(get_all_range([], range(1, 5)), [])


class TestGetAllNotInRange(unittest.TestCase):
    def test_default_range(self):
        numbers = [-3, -1, 0, 2, 4, 7]
        self.assertEqual(get_all_not_in_range(numbers), numbers)

    def test_partial_exclusion(self):
        self.assertEqual(
            get_all_not_in_range([-3, -1, 0, 2, 4, 7], range(-1, 4)),
            [-3, 4, 7],
        )

    def test_empty_range(self):
        numbers = [-2, 0, 3]
        self.assertEqual(get_all_not_in_range(numbers, range(1, 1)), numbers)

    def test_exclude_all(self):
        self.assertEqual(
            get_all_not_in_range([1, 2, 3], range(0, 5)),
            [],
        )

    def test_no_matches(self):
        self.assertEqual(
            get_all_not_in_range([-5, -2, 0], range(1, 4)),
            [-5, -2, 0],
        )

    def test_empty_numbers(self):
        self.assertEqual(get_all_not_in_range([], range(-2, 3)), [])


class TestMySorted(unittest.TestCase):
    def test_empty_items(self):
        self.assertEqual(my_sorted([]), [])

    def test_single_item(self):
        self.assertEqual(my_sorted([7]), [7])

    def test_two_chunks(self):
        self.assertEqual(my_sorted([4, 1, 3, 2]), [1, 4, 2, 3])

    def test_full_chunks(self):
        items = [6, 1, 5, 2, 4, 3, 9, 7, 8]
        self.assertEqual(
            my_sorted(items),
            [1, 5, 6, 2, 3, 4, 7, 8, 9],
        )

    def test_short_last_chunk(self):
        items = [9, 1, 7, 6, 0, 8, 5, 2, 4, 3]
        self.assertEqual(
            my_sorted(items),
            [1, 7, 9, 0, 6, 8, 2, 3, 4, 5],
        )

    def test_duplicates(self):
        items = [4, 1, 4, 2, 3, 1, 2, 3, 1]
        self.assertEqual(
            my_sorted(items),
            [1, 4, 4, 1, 2, 3, 1, 2, 3],
        )

    def test_key_function(self):
        items = [-8, 3, -1, 6, 2, -4, 5, -7, 0]
        self.assertEqual(
            my_sorted(items, key=abs),
            [-1, 3, -8, 2, -4, 6, 0, 5, -7],
        )

    def test_tuple_key(self):
        items = [
            ("pear", 4), ("apple", 1), ("fig", 3),
            ("plum", 0), ("lime", 5), ("date", 2),
        ]
        self.assertEqual(
            my_sorted(items, key=lambda item: item[0]),
            [
                ("apple", 1), ("pear", 4), ("fig", 3),
                ("plum", 0), ("date", 2), ("lime", 5),
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)