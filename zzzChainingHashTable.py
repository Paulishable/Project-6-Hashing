from hashmap import HashTable


class ChainingHashTableItem:
    def __init__(self, itemKey, itemValue):
        self.key = itemKey
        self.value = itemValue
        self.next = None

    def __str__(self):
        if self.next is not None:
            return self.key + ", " + self.value + " --> " + self.next.key + ",  " + self.next.value
        return str(self.key) + ", " + str(self.value)


class ChainingHashTable(HashTable):
    def __init__(self, initialCapacity=11):
        self.table = [None] * initialCapacity

    def __str__(self):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                print(self.table[i])
            else:
                print("(empty)")
        return ""

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def set(self, key, value):
        """add the (key,value) pair to the hashMap.
        After adding, if the load-factor >= 80%,
        rehash the map into a map double its current capacity."""
        # Hash the key to get the bucket index
        bucket_index = self.get(key) % len(self.table)

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

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        # Hash the key to get the bucket index
        bucket_index = self.get(key) % len(self.table)

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

    # Searches for the key, returning the corresponding value if found, None if
    # not found.
    def search(self, key):
        # Hash the key to get the bucket index
        bucket_index = self.get(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        while item is not None:
            if key == item.key:
                return item.value
            item = item.next
        return None  # key not found

    def clear(self):
        """empty the HashMap"""
        self.__init__(11)
        return self

    def get(self, key):
        return self.search(key)
