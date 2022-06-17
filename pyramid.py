from DictionaryFunctions import test_the_dictionary, set_dictionary_pyramid_depth
from NoHashingFunctions import test_no_hashing, set_no_hashing_pyramid_depth
from ChainHashFunctions import test_the_chain_hash, set_chain_pyramid_depth

import sys

PYRAMID_DEPTH = 7
if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])

set_dictionary_pyramid_depth(PYRAMID_DEPTH)
set_no_hashing_pyramid_depth(PYRAMID_DEPTH)
set_chain_pyramid_depth(PYRAMID_DEPTH)


test_no_hashing()

test_the_dictionary()

test_the_chain_hash()
