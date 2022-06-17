from pyramid import *

global dictionary
dictionary = {}
for i in range(0, PYRAMID_DEPTH):
    for j in range(0, PYRAMID_DEPTH):
        dictionary[(i, j)] = -1.0


def print_dictionary():
    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, PYRAMID_DEPTH):
            print("i,j = ", i, j, dictionary[(i, j)])


def weight_on_dict(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls, dictionary, cache_hits
    function_calls += 1

    if dictionary[(row, column)] != -1.0:
        cache_hits += 1
        return dictionary[(row, column)]

    # case 1 top person
    if row == 0:
        weight = 0.0
        dictionary[(row, column)] = weight
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


def print_the_weight_calculations_with_dictionary():
    global function_calls, dictionary, cache_hits
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on_dict(i, j)), end=" ")
