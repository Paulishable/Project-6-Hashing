from settings import *

if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])


def weight_on(row, column):
    """calculate the weight on each person in the pyramid"""
    global function_calls, chain_hash, cache_hits
    function_calls += 1

    if chain_hash.search((row, column)) is not None:
        cache_hits += 1
        return chain_hash.search((row, column))

    # case 1 top person
    if row == 0:
        chain_hash.set((row, column), 0.0)
        return 0.0

    # case 2 person on left edge
    if column == 0:
        weight = (PERSON_WEIGHT + weight_on(row - 1, column)) / 2
        chain_hash.set((row, column), weight)
        return weight

    # case 3 person on  right edge
    if column == row:
        weight = (PERSON_WEIGHT + weight_on(row - 1, column - 1)) / 2
        chain_hash.set((row, column), weight)
        return weight

    # case 4 internal person  --- everyone else is calculated here
    weight = (PERSON_WEIGHT + weight_on(row - 1, column)) / 2 + (
            PERSON_WEIGHT + weight_on(row - 1, column - 1)) / 2
    chain_hash.set((row, column), weight)
    return weight


def run_the_weight_calculations_with_hashing():
    global function_calls, cache_hits, chain_hash
    function_calls = cache_hits = 0
    chain_hash.clear()

    for i in range(0, PYRAMID_DEPTH):
        for j in range(0, i + 1):
            if i == 0:
                pass
            if i == j:
                weight_on(i, j)
            if i != 0 and i != j:
                weight_on(i, j)


def print_the_weight_calculations_with_hashing():
    global function_calls, dictionary, cache_hits
    function_calls = cache_hits = 0

    for i in range(0, PYRAMID_DEPTH):
        print(" ")
        for j in range(0, i + 1):
            print(f" %6.2f" % (weight_on(i, j)), end=" ")


# # print_the_weight_calculations()
# start = perf_counter()
# run_the_weight_calculations()
# end = perf_counter()
# print()
# print("function calls = ", function_calls)
# print("cache hits = ", cache_hits)
# print(f"\n NO caching Time for Pyramid height of {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
# #
# start = perf_counter()
# run_the_weight_calculations_with_dictionary()
# end = perf_counter()
# # # print_the_weight_calculations_with_dictionary()
# #
# print(len(dictionary))
# print(dictionary)
# print("with Dictionary - function calls = ", function_calls)
# print("cache hits = ", cache_hits)
# print(f"\n with Dictionary - Time for Pyramid height of {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
# #
# # print_the_weight_calculations()
# # print_the_weight_calculations_with_dictionary()
#
#
#
# print_the_weight_calculations_with_hashing()
#
# start = perf_counter()
# run_the_weight_calculations_with_hashing()
# end = perf_counter()
# print()
# print("function calls = ", function_calls)
# print("cache hits = ", cache_hits)
# print(f"\n HASHING Time for Pyramid height of {PYRAMID_DEPTH}      = ", "%.6f" % (end - start), "seconds")
#
# print("\n\n\n\n")
# print("Capcity: ", chain_hash.capacity())
# print("size is: ", chain_hash.size())
#
# load = chain_hash.size() / chain_hash.capacity()
#
# print(" load is ", load, "\n")
#
# print("----------------RESIZING-------------------")
# # chain_hash.resize_hashtable()
#
# print("Capcity: ", chain_hash.capacity())
# print("size is: ", chain_hash.size())
#
# load = chain_hash.size() / chain_hash.capacity()
#
# print("\n load is ", load)
#
# # chain_hash.__str__()
#
# print("\n KEYS and VALUES are:")
#
# print(chain_hash.keys())
# print(chain_hash.values())
#
# print("----------------RESIZING-------------------")
# # chain_hash.resize_hashtable()
#
# print("Capcity: ", chain_hash.capacity())
# print("size is: ", chain_hash.size())
#
# load = chain_hash.size() / chain_hash.capacity()
#
# print("\n load is ", load)
#
# # chain_hash.__str__()
#
# print("\n KEYS and VALUES are:")
#
# print(chain_hash.keys())
# print(chain_hash.values())

keys = [(r, r) for r in (range(10))]
values = list(range(1, 11))
hm = HashMap()
for k, v in zip(keys, values):
    hm.set(k, v)

print(hm.get((2, 2)), "a val")

print("size", hm.size())
print("capacity", hm.capacity())
assert hm.size() == 10
assert hm.capacity() == 13
