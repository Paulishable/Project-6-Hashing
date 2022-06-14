from time import perf_counter

PERSON_WEIGHT = 200.0
PYRAMID_DEPTH = 23
function_calls = 0


def weight_on(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls
    function_calls += 1
    # case 1 top person
    if row == 0:
        return 0.0

    # case 2 person on left edge
    if column == 0:
        weight = (PERSON_WEIGHT + weight_on(row - 1, column)) / 2
        return weight

    # case 3 person on  right edge
    if column == row:
        weight = (PERSON_WEIGHT + weight_on(row - 1, column - 1)) / 2
        return weight

    # case 4 internal person  --- everyone else is calculated here
    weight = (PERSON_WEIGHT + weight_on(row - 1, column)) / 2 + (PERSON_WEIGHT + weight_on(row - 1, column - 1)) / 2

    return weight


start = perf_counter()

print("For a pyramid of height = 7:", end=" ")
for i in range(0, PYRAMID_DEPTH):
    print()
    for j in range(0, i + 1):
        print(f" %.2f" % (weight_on(i, j)), end=" ")

end = perf_counter()
print()
print("function calls = ", function_calls)
print(f"\n Pyramid height = {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
