# Base class for a hash table that supports the insert, remove, and search
# operations.
class HashTable:
    # Returns a non-negative hash code for the specified key.
    def get(self, key):
        """Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError."""
        return abs(hash(key))

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def set(self, key, value):
        """add the (key,value) pair to the hashMap.
        After adding, if the load-factor >= 80%,
        rehash the map into a map double its current capacity."""
        pass

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        """Remove the key and its associated value from the map.
        If the key does not exist, nothing happens.
        Do not rehash the table after deleting keys."""
        pass

    def clear(self, key):
        """empty the HashMap"""
        pass

    def capacity(self):
        """Return the current capacity--number of buckets--in the map."""
        pass

    def size(self):
        """Return the number of key-value pairs in the map."""
        return 99999

    def keys(self):
        """Return a list of keys."""
        pass