from DictionaryFunctions import *
from NoHashingFunctions import *
from ChainHashFunctions import *

if __name__ == '__main__':
    if len(sys.argv) != 1:
        PYRAMID_DEPTH = int(sys.argv[1])

test_no_hashing()

test_the_dictionary()

test_the_chain_hash()
