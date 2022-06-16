# Base class for a hash table that supports the insert, remove, and search
# operations.
class HashTable:
    # Returns a non-negative hash code for the specified key.
    def get2(self, key):
        """Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError."""
        return abs(hash(key))

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        """Remove the key and its associated value from the map.
        If the key does not exist, nothing happens.
        Do not rehash the table after deleting keys."""
        pass

    def capacity(self):
        """Return the current capacity--number of buckets--in the map."""
        return len(self.table)

    def size(self):
        """Return the number of key-value pairs in the map."""
        counter = 0
        for item in self.table:
            if item is not None:
                counter += 1
        return counter

    def keys(self):
        """Return a list of keys."""
        list_of_keys = []

        for i in range(len(self.table)):
            item = self.table[i]
            if item is not None:
                while item is not None:
                    list_of_keys.append(item.key)
                    item = item.next
        return list_of_keys

    def values(self):
        """Return a corresponding list of values."""
        list_of_values = []

        for i in range(len(self.table)):
            item = self.table[i]
            if item is not None:
                while item is not None:
                    list_of_values.append(item.value)
                    item = item.next
        return list_of_values



