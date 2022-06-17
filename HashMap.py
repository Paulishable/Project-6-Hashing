""" the chaining hash table class"""


class ChainingHashTableItem:
    """an item in the chaining hashtable -- it is a linked list node"""
    def __init__(self, item_key, item_value):
        self.key = item_key
        self.value = item_value
        self.next = None

    def __str__(self):
        return str(self.key) + ", " + str(self.value)

    def get_key(self):
        """return key"""
        return self.key

    def get_value(self):
        """return value"""
        return self.value


class HashMap():
    """the class for the chaining hash table"""
    def __init__(self, initial_capacity=7):
        self.table = [None] * initial_capacity

    def __str__(self):
        for item in self.table:
            if item is not None:
                while item is not None:
                    print(item)
                    item = item.next
            else:
                print("(empty)")
        return ""

    def print(self):
        """print the hash table itself"""
        self.__str__()
        return ""

    def hashkey(self, key):
        """Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError."""
        r_val = 2
        sum_of_parts = key[0] + key[1]
        squared_key = sum_of_parts * sum_of_parts

        low_bits_to_remove = (32 - r_val) // 2
        extracted_bits = squared_key >> low_bits_to_remove
        extracted_bits = extracted_bits & (0xFFFFFFFF >> (32 - r_val))
        return extracted_bits % len(self.table)

    def capacity(self):
        """Return the current capacity--number of buckets--in the map."""
        return len(self.table)

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def set(self, key, value):
        """insert a value into the table
        resize if needed load factor must be less than 80%"""

        the_capacity = self.capacity()
        the_size = self.size()
        load = the_size / the_capacity
        while load >= .8:
            self.resize_hashtable()
            the_capacity = self.capacity()
            the_size = self.size()
            load = the_size / the_capacity

        # Hash the key to get the bucket index
        bucket_index = self.hashkey(key)
        # bucket_index = self.get2(key) % len(self.table)

        # Traverse the linked list, searching for the key. If the key exists in
        # an item, the value is replaced. Otherwise a new item is appended.
        item = self.table[bucket_index]
        previous = None
        while item is not None:
            if key == item.key:
                item.value = value
                return True

            previous = item
            item = item.next

        # Append to the linked list
        if self.table[bucket_index] is None:
            self.table[bucket_index] = ChainingHashTableItem(key, value)
        else:
            previous.next = ChainingHashTableItem(key, value)
        return True

    def remove(self, key):
        """Searches for the specified key. If found, the key/value pair is removed
    from the hash table and True is returned. If not found, False is returned."""
        # Hash the key to get the bucket index
        bucket_index = self.hashkey(key)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        previous = None
        while item is not None:
            if key == item.key:
                if previous is None:
                    # Remove linked list's first item
                    self.table[bucket_index] = item.next
                else:
                    previous.next = item.next
                return True
            previous = item
            item = item.next
        return False  # key not found

    def search(self, key):
        """Searches for the key, returning the corresponding value if found, None if not found."""
        # Hash the key to get the bucket index
        bucket_index = self.hashkey(key)
        # bucket_index = self.get2(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        while item is not None:
            if key == item.key:
                return item.value
            item = item.next
        return None  # key not found

    def get(self, key):
        """find and return an item in the table"""
        value = self.search(key)
        if value is None:
            raise KeyError("KeyError exception thrown")

        return value

    def clear(self):
        """empty the HashMap"""
        self.__init__()
        return self

    def resize_hashtable(self):
        """lower load factor by doubling buckets and subtracting one from that"""
        new_capacity = 2 * self.capacity() - 1
        list_keys_from_old_table = self.keys()
        list_values_from_old_table = self.values()

        self.__init__(new_capacity)

        for i in range(len(list_keys_from_old_table)):
            self.set(list_keys_from_old_table[i], list_values_from_old_table[i])

        return self

    def size(self):
        """Return the number of key-value pairs in the map."""
        the_size = len(self.keys())
        # counter = 0
        # for item in self.table:
        #     if item is not None:
        #         print("inner loop", item.key)
        #         counter += 1
        # return counter
        return the_size

    def keys(self):
        """Return a list of keys."""
        list_of_keys = []

        # for i in range(len(self.table)):
        for item in self.table:
            if item is not None:
                while item is not None:
                    list_of_keys.append(item.key)
                    item = item.next
        return list_of_keys

    def values(self):
        """Return a corresponding list of values."""
        list_of_values = []

        for item in self.table:
            if item is not None:
                while item is not None:
                    list_of_values.append(item.value)
                    item = item.next
        return list_of_values
