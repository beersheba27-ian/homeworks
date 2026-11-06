from functions import *


if __name__ == "__main__":
    print("-------- max_with_negative_duplicate debug print --------")
    print(
        max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]),
        "| expected 100",
    )
    print(max_with_negative_duplicate([3, -3, 5, -5]), "| expected 5")
    print(max_with_negative_duplicate([1, 2, 3]), "| expected -1")
    print(max_with_negative_duplicate([]), "| expected -1")
    print()

    print("-------- sumOfTwoExists debug print --------")
    print(sumOfTwoExists([1, -1, 40, 50, 0], 0), "| expected True")
    print(sumOfTwoExists([1, -1, 40, 50, 0], 42), "| expected False")
    print(sumOfTwoExists([1, -1, 40, 50, 0], 39), "| expected True")
    print(sumOfTwoExists([3, 3], 6), "| expected True")
    print(sumOfTwoExists([0], 0), "| expected False")
    print(sumOfTwoExists([], 0), "| expected False")
    print()

    print("-------- bubble_sort debug print --------")
    numbers = [4, 2, 3, 1]
    bubble_sort(numbers)
    print(numbers, "| expected [1, 2, 3, 4]")

    numbers = [1, 2, 3]
    bubble_sort(numbers)
    print(numbers, "| expected [1, 2, 3]")

    numbers = [3, 2, 2, -1]
    bubble_sort(numbers)
    print(numbers, "| expected [-1, 2, 2, 3]")

    numbers = [7]
    bubble_sort(numbers)
    print(numbers, "| expected [7]")

    numbers = []
    bubble_sort(numbers)
    print(numbers, "| expected []")
    print()

    print("-------- remove_duplicates debug print --------")
    print(
        remove_duplicates([-1, 0, 100, -1, 20, 80, 20]),
        "| expected [-1, 0, 100, 20, 80]",
    )
    print(remove_duplicates([1, 2, 3]), "| expected [1, 2, 3]")
    print(remove_duplicates([5, 5, 5]), "| expected [5]")
    print(remove_duplicates([]), "| expected []")
