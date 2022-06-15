from time import perf_counter
import sys
from ChainingHashTable import *

PERSON_WEIGHT = 200.0
PYRAMID_DEPTH = 7
global function_calls, cache_hits
function_calls = 0
cache_hits = 0

global dictionary
dictionary = {}
for i in range(0, PYRAMID_DEPTH):
    for j in range(0, PYRAMID_DEPTH + 1):
        dictionary[(i, j)] = -1.0


def print_dictionary():
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, PYRAMID_DEPTH + 1):
            print("i,j = ", i, j, dictionary[(i, j)])


if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])


def weight_on_dict(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls, dictionary, cache_hits
    function_calls += 1

    if dictionary[(row, column)] != -1.0:
        cache_hits += 1
        return dictionary[(row, column)]

    # case 1 top person
    if row == 0:
        dictionary[(row, column)] = 0.0
        return 0.0

    # case 2 person on left edge
    if column == 0:
        weight = (PERSON_WEIGHT + weight_on_dict(row - 1, column)) / 2
        dictionary[(row, column)] = weight
        return weight

    # case 3 person on  right edge
    if column == row:
        weight = (PERSON_WEIGHT + weight_on_dict(row - 1, column - 1)) / 2
        dictionary[(row, column)] = weight
        return weight

    # case 4 internal person  --- everyone else is calculated here
    weight = (PERSON_WEIGHT + weight_on_dict(row - 1, column)) / 2 + (
                PERSON_WEIGHT + weight_on_dict(row - 1, column - 1)) / 2
    dictionary[(row, column)] = weight
    return weight


def weight_on(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls
    function_calls += 1
    # case 1 top person
    if row == 0:
        weight = 0.0
        return weight

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


def write_the_weight_calculations_to_a_file():
    global function_calls
    function_calls = 0

    print("For a pyramid of height = 7:", end=" ")
    for i in range(1, PYRAMID_DEPTH):
        print()
        for j in range(0, i + 1):
            print(f" %.2f" % (weight_on(i, j)), end=" ")


def run_the_weight_calculations():
    global function_calls, cache_hits
    function_calls = cache_hits = 0
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on(i, j)
            if i != 0 and i != j:
                weight_on(i, j)


def run_the_weight_calculations_with_dictionary():
    global function_calls, cache_hits, dictionary
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on_dict(i, j)
            if i != 0 and i != j:
                weight_on_dict(i, j)


def print_the_weight_calculations():
    global function_calls, dictionary, cache_hits
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on(i, j)), end=" ")


def print_the_weight_calculations_with_dictionary():
    global function_calls, dictionary, cache_hits
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on_dict(i, j)), end=" ")


#
# # print_the_weight_calculations()
# start = perf_counter()
# run_the_weight_calculations()
# end = perf_counter()
# print()
# print("function calls = ", function_calls)
# print("cache hits = ", cache_hits)
# print(f"\n Time for Pyramid height of {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
#
# start = perf_counter()
# run_the_weight_calculations_with_dictionary()
# end = perf_counter()
# # print_the_weight_calculations_with_dictionary()
#
# print()
# print("with Dictionary - function calls = ", function_calls)
# print("cache hits = ", cache_hits)
# print(f"\n with Dictionary - Time for Pyramid height of {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
#
# print_the_weight_calculations()
# print_the_weight_calculations_with_dictionary()


my_hasher = ChainingHashTable(20)

my_hasher.insert((1, 0), 100.0)
my_hasher.insert((2, 1), 300.0)
# Print each table's buckets again
print("")
print(my_hasher)
print(my_hasher.size())
print(my_hasher.search((2,1)))
my_hasher.remove((2, 1))
print(my_hasher.search((2,1)))


