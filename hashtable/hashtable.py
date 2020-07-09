class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = 0
        self.storage = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        h = 5381
        for s in key:
            h = ((h << 5) + h) + ord(s)
        return h % 0x100000000


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.elements += 1
        new_item = HashTableEntry(key, value)
        location = self.hash_index(key)
        # gets current location in storage
        current = self.storage[location]

        # check if anything is there, if not insert linked list (HashTableEntry)
        if not current:
            self.storage[location] = new_item
        # otherwise, traverse until end, and update (rewrite recursively)
        else:
            while current.next:
                current = current.next
            current.next = new_item

        # CHECK LOAD FACTOR > 0.7
        current_load_factor = self.get_load_factor()
        if current_load_factor > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        location = self.hash_index(key)
        target = self.storage[location]

        if target.key == key:
            self.elements -= 1
            if not target.next:
                target.key = target.value = None
            else:
                self.storage[location] = target.next
        else:
            current_item = target
            next_item = target.next
            while next_item:
                if next_item.key == key:
                    self.elements -= 1
                    current_item.next = next_item.next
                    break
                current_item = next_item
                next_item = next_item.next
            print(f"{key} not found")

        # CHECK LOAD FACTOR < 0.2



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        target = self.storage[self.hash_index(key)]

        while target:
            if target.key == key:
                return target.value
            target = target.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_table = HashTable(new_capacity)

        for item in self.storage:
            if item:
                new_table.put(item.key, item.value)
                if item.next:
                    next_item = item.next
                    while next_item:
                        new_table.put(next_item.key, next_item.value)
                        next_item = next_item.next
        
        self.storage = new_table.storage
        del new_table



if __name__ == "__main__":
    ht = HashTable(MIN_CAPACITY)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    ht.delete("line_12")
    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))