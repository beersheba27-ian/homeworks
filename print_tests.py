from functions import *
# print calls for testing the functions from the file functions.py


if __name__ == "__main__":
    # intersection
    print("---------- intersection debug print ----------")
    print(str(intersection([1, 2, 3], [4, 3, 1])) + " | expected [1, 3]")
    print(str(intersection([1, 2, 3], [4, 5, 6])) + " | expected []")
    print(str(intersection([], [1, 2, 3])) + " | expected []")
    print()

    # union
    print("---------- union debug print ----------")
    print(str(union([1, 2, 3], [4, 3, 1])) + " | expected [1, 2, 3, 4]")
    print(str(union([1, 2, 3], [4, 5, 6])) + " | expected [1, 2, 3, 4, 5, 6]")
    print(str(union([], [-2, 0, 3])) + " | expected [-2, 0, 3]")
    print(str(union([1, 2], [2, 1])) + " | expected [1, 2]")
    print(str(union([1, 2], [1, 2])) + " | expected [1, 2]")
    print()

    # difference
    print("---------- difference debug print ----------")
    print(str(difference([1, 2, 3], [4, 3, 1])) + " | expected [2]")
    print(str(difference([1, 2, 3], [4, 5, 6])) + " | expected [1, 2, 3]")
    print(str(difference([], [1, 2, 3])) + " | expected []")
    print(str(difference([-3, 0, 4], [0])) + " | expected [-3, 4]")
    print()

    # symmetric_difference
    print("---------- symmetric_difference debug print ----------")
    print(str(symmetric_difference([1, 2, 3], [4, 3, 1])) + " | expected [2, 4]")
    print(str(symmetric_difference([1, 2, 3], [4, 5, 6])) + " | expected [1, 2, 3, 4, 5, 6]")
    print(str(symmetric_difference([1, 2], [1, 2])) + " | expected []")
    print(str(symmetric_difference([], [-2, 0, 3])) + " | expected [-2, 0, 3]")
    print()

    # remove_positive_greater_or_negative_less
    print("---------- remove_positive_greater_or_negative_less debug print ----------")
    print(str(remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)) + " | expected [1, 2, -3, 10]")
    print(str(remove_positive_greater_or_negative_less([-4, -3, 0, 10, 11], 10, -3)) + " | expected [-3, 0, 10]")
    print(str(remove_positive_greater_or_negative_less([], 10, -3)) + " | expected []")
    print(str(remove_positive_greater_or_negative_less([0, -1, 1], 0, -1)) + " | expected [0, -1]")
    print()

    # max_with_negative_duplicate
    print("---------- max_with_negative_duplicate debug print ----------")
    print(str(max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])) + " | expected 100")
    print(str(max_with_negative_duplicate([10, 20, -15, -11, 20])) + " | expected -1")
    print(str(max_with_negative_duplicate([])) + " | expected -1")
    print(str(max_with_negative_duplicate([-5, 5, -8, 8])) + " | expected 8")
    print()
