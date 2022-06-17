from HashMap import *
from time import perf_counter
import sys

PERSON_WEIGHT = 200.0
PYRAMID_DEPTH = 7
global function_calls, cache_hits, chain_hash

chain_hash = HashMap()

function_calls = 0
cache_hits = 0