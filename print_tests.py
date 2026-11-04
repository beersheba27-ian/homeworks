from functions import *

if __name__ == "__main__":
    print("-------- minMaxAverage debug print --------")
    print(minMaxAverage([1, 2, 3, 4, 5]), "| expected (1, 5, 3.0)")
    print(minMaxAverage([7]), "| expected (7, 7, 7.0)")
    print(minMaxAverage([-8, -3, -5]), "| expected (-8, -3, -5.333333333333333)")
    print(minMaxAverage([]), "| expected (None, None, None)")
    print()

    print("-------- moveMaxToEnd debug print --------")
    numbers = [100, 20, 30, 40, 50]
    moveMaxToEnd(numbers)
    print(numbers, "| expected [20, 30, 40, 50, 100]")

    numbers = [1, 5, 2, 5, 3]
    moveMaxToEnd(numbers)
    print(numbers, "| expected [1, 2, 3, 5, 5]")

    numbers = [4, 4, 4]
    moveMaxToEnd(numbers)
    print(numbers, "| expected [4, 4, 4]")

    numbers = [-7, -2, -5]
    moveMaxToEnd(numbers)
    print(numbers, "| expected [-7, -5, -2]")

    numbers = [9]
    moveMaxToEnd(numbers)
    print(numbers, "| expected [9]")

    numbers = []
    moveMaxToEnd(numbers)
    print(numbers, "| expected []")
    print()
