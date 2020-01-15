'''
Linked List hash table key/value pair
'''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        # 2nd Stretch Goal
        self.entries = 0  # Track entries to auto resize
        self.start_capacity = capacity # Save initial capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        https://stackoverflow.com/a/13809282/11304328
        Start from Magic Constant 5831
        1. odd number
        2. prime number
        3. deficient number
        4. 001/010/100/000/101 b
        '''
        # Cast the key to a string
        str_key = str(key)
        # Start from Magic Constant 5831
        djb2_hash = 5381
        # Bit-shift and sum value for each character
        for char in str_key:
            # djb2_hash = ((djb2_hash << 5) + djb2_hash) + ord(char)
            djb2_hash = (djb2_hash * 33) + ord(char)
        return djb2_hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        # double in size automatically when hashtable
        # grows past a load factor of 0.7
        if self.entries / self.capacity > .7:
            self.resize(2)

        index = self._hash_mod(key)
        current = self.storage[index]
        # Insert value
        if current:
            while current.key != key and current.next:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = LinkedPair(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)

        self.entries += 1

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        if key == current.key:
            self.storage[index] = self.storage[index].next
            self.entries -= 1

        while current.next:
            if key == current.next.key:
                current.next = current.next.next
                self.entries -= 1
                return
            else:
                current = current.next

        # half in size when it shrinks past a load factor of 0.2
        # This should only occur if the HashTable
        # has been resized past the initial size
        if ((self.start_capacity != self.capacity) &
                (self.entries / self.capacity < .2)):
            self.resize(.5)

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        while current:
            if key == current.key:
                return current.value
            current = current.next

        return

    def resize(self, factor):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity = int(self.capacity * factor)
        prev_storage = self.storage
        self.storage = [None] * self.capacity

        for current in prev_storage:
            while current:
                self.insert(current.key, current.value)
                current = current.next

        # Reset entries
        self.entries = 0


if __name__ == "__main__":
    ht = HashTable(10)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    # ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print(ht._hash_mod("key-9"))
    print(ht._hash_mod("key-8"))
    print(ht._hash_mod("key-7"))
    print(ht._hash_mod("key-6"))
    print(ht._hash_mod("key-5"))
    print(ht._hash_mod("key-4"))
    print(ht._hash_mod("key-3"))
    print(ht._hash_mod("key-2"))
    print(ht._hash_mod("key-1"))
    print(ht._hash_mod("key-0"))
