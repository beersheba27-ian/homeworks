def binary_search(numbers: list[int], num:int)->int:
    """
    O[logN]
    numbers: sorted list
    num: being searched number
    returns an index of the first occurrence at which "num" resides in "numbers" or 
    negative number as -(index_sort + 1) where index_sort is the index where "num" should have been in "numbers"
    for example: numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
    binary_search(numbers, 20) -> 3 (not 4),binary_search(numbers, 15) -> -4 (not -1),
    binary_search(numbers, 45) -> -10
    """    
    left: int = 0
    right: int = len(numbers) - 1
    target: int = (left + right) // 2
    while left <= right and numbers[target] != num:
        if num < numbers[target]:
            right = target - 1
        else:
            left = target + 1
        target = (left + right) // 2
    if left <= right:
        while numbers[target] == numbers[target-1] and target > 0:
            target -=1
    else:
        target = -(target + 2)
    return target

def insert_sorted(numbers: list[int], num: int) -> None:
    """
    numbers: sorted list
    num: inserted number
    inserts "num" keeping "numbers" sorted
    For example: numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 19) the list will contain [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 20) (initial list) the list will contain [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]

    """   