from settings import *
from time import perf_counter


def weight_on_without(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls
    function_calls += 1
    # case 1 top person
    if row == 0:
        weight = 0.0
        return weight

    # case 2 person on left edge
    if column == 0:
        weight = (PERSON_WEIGHT + weight_on_without(row - 1, column)) / 2
        return weight

    # case 3 person on  right edge
    if column == row:
        weight = (PERSON_WEIGHT + weight_on_without(row - 1, column - 1)) / 2
        return weight

    # case 4 internal person  --- everyone else is calculated here
    weight = (PERSON_WEIGHT + weight_on_without(row - 1, column)) / 2 + (
            PERSON_WEIGHT + weight_on_without(row - 1, column - 1)) / 2
    return weight


def write_the_weight_calculations_to_a_file():
    global function_calls
    f = open("part2.txt", "a")

    for i in range(0, PYRAMID_DEPTH):
        f.write("\n")
        for j in range(0, i + 1):
            f.write("{:6.2f} ".format(weight_on_without(i, j)))

    start = perf_counter()
    run_the_weight_calculations()
    end = perf_counter()
    f.write(" ")
    f.write("\nElapsed time: {:6.7f}".format((end - start)))
    f.write(f"\nNumber of function calls : {function_calls}")


def run_the_weight_calculations():
    global function_calls, cache_hits
    function_calls = cache_hits = 0
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on_without(i, j)
            if i != 0 and i != j:
                weight_on_without(i, j)


def print_the_weight_calculations():
    global function_calls, dictionary, cache_hits
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on_without(i, j)), end=" ")
