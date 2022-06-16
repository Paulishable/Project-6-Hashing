from hashmap import HashTable


class ChainingHashTableItem:
    def __init__(self, item_key, item_value):
        self.key = item_key
        self.value = item_value
        self.next = None

    def __str__(self):
        return str(self.key) + ", " + str(self.value)


class ChainingHashTable(HashTable):
    def __init__(self, initial_capacity=7):
        self.table = [None] * initial_capacity
        print("from init", initial_capacity)

    def __str__(self):
        for i in range(len(self.table)):
            item = self.table[i]
            if item is not None:
                while item is not None:
                    print(item)
                    item = item.next
            else:
                print("(empty)")
        return

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def set(self, key, value):
        # resize if needed load factor must be less than 80%
        the_capacity = self.capacity()
        the_size = self.size()
        load = the_size / the_capacity
        while load >= .8:
            print("here")
            self.resize_hashtable()
            the_capacity = self.capacity()
            the_size = self.size()
            load = the_size / the_capacity

        # Hash the key to get the bucket index
        # bucket_index = self.hashKey(key) % len(self.table)
        bucket_index = self.get2(key) % len(self.table)

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
        bucket_index = self.hashKey(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        previous = None
        while item is not None:
            if key == item.key:
                if previous == None:
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
        # bucket_index = self.hashKey(key) % len(self.table)
        bucket_index = self.get2(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        while item is not None:
            if key == item.key:
                return item.value
            item = item.next
        return None  # key not found

    def get(self, key):
        value = self.search(key)
        if value is None:
            raise KeyError

        return value

    def clear(self):
        """empty the HashMap"""
        self.__init__()
        return self

    def resize_hashtable(self):
        """lower load factor by doubling buckets and subtracting one from that"""
        new_capacity = 2 * self.capacity() - 1
        print("new capacity", new_capacity)
        list_keys_from_old_table = self.keys()
        list_values_from_old_table = self.values()

        self.__init__(new_capacity)

        for i in range(len(list_keys_from_old_table)):
            self.set(list_keys_from_old_table[i], list_values_from_old_table[i])

        # for i in range(len(self.table)):
        #     if self.table[i] is not None:
        #         list_items_from_old_table.append(str(self.table[i].key) + ", " + str(self.table[i].value))
        #         enumerator = self.table[i].next
        #         if enumerator is not None:
        #             list_items_from_old_table.append(
        #                 str(self.table[i].next.key) + ",  " + str(self.table[i].next.value))
        #             enumerator = self.table[i].next.next
        #
        # # self.__init__(new_capacity)
        #
        # the_keys = self.keys()
        # # print("the keys", str(self.__str__()))
        # print(list_items_from_old_table)

        return self
