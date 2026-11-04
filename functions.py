# the function call should be like: min, max, average = minMaxAverage(...), 
# think of arguments instead of dots, and think of parameters at a function definition, 
# and think what the function should return (which type). 
# Note: average variable should contain float while min, max are integers
def minMaxAverage(numbers: list[int]) -> tuple[int, int, float] | tuple[None, None, None]:
    result = (None, None, None)
    if numbers:
        result = (min(numbers), max(numbers), sum(numbers) / len(numbers))
    return result

# the function takes reference to a list
# the function returns nothing
# the function moves maximal element to the end of a list
# example
# l1: list[int]=[100, 20, 30, 40, 50]
# moveMaxToEnd(l1)
# after the above function call l1 shoild be bound to the list [20, 30, 40, 50, 100]
def moveMaxToEnd(numbers: list[int]) -> None:
    if not numbers:
        return
    max_elem = max(numbers)
    max_count = numbers.count(max_elem)
    i = 0
    while i < max_count:
        numbers.remove(max_elem)
        numbers.append(max_elem)
        i += 1