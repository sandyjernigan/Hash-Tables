# '''
# Linked List hash table key/value pair
# '''
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


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # Starter has value
        hash_value = 2020

        # Bit-shift and sum value for each character
        for char in str(key):
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        ''' Store the value with the given key. '''
        newPair = LinkedPair(key, value)

        # Get the index using hash mod
        index = self._hash_mod(key)
        
        # Node for this index
        node = self.storage[index]

        # If bucket is empty
        if node is None:

            # Create the node
            self.storage[index] = newPair
            return

        ''' Part 1: Hash collisions should be handled with an error warning. '''
        # If node already exists
        while node is not None:

            # Check if key matchs
            if node.key == key:

                # replace value if key matches
                self.storage[index] = newPair
                return

            ''' Part 2: Change this so that hash collisions are handled with Linked List Chaining. '''
            # Otherwise, Add Node to end of the list
            prev = node
            node = node.next
        
        prev.next = newPair

    def remove(self, key):
        ''' Remove the value stored with the given key. '''
        
        # Get the index using hash mod
        index = self._hash_mod(key)
        
        # Node for this index
        node = self.storage[index]

        # Set initial point
        prev = None

        # Traverse the list, til node is None, or key is found
        while node is not None:
            prev = node

            # Check if key matchs 
            if node.key == key:

                if node.next is not None:
                    prev.next = prev.next.next

                # Delete the node
                self.storage[index] = None
                return
            
            # If not found, go to next
            node = node.next
        
        ''' Print a warning if the key is not found. '''
        # If at end and key not found, print warning
        print(f'Key not Found.')
        return None

    def retrieve(self, key):
        ''' Retrieve the value stored with the given key. '''
        # Get the index using hash mod
        index = self._hash_mod(key)

        # Get Node for this index
        node = self.storage[index]

        ''' Returns None if the key is not found. '''
        if node is None:
            return None

        # Traverse the list, til node is None, or key is found
        while node is not None:

            # Check if key matches 
            if node.key == key:

                # key found, return value
                return node.value
            
            # If not found, go to next
            node = node.next

        ''' Returns None if the key is not found in the list. '''
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        # Old Storage
        old_storage = self.storage

        # Double the capacity
        self.capacity *= 2

        # New Table with Double capacity
        self.storage = [None] * self.capacity

        # For each node in HashTable
        for each in old_storage:

            # Check each node, if not None
            node = each
            while node is not None:
            
                # Rehash key/value pair and Insert into the new table
                self.insert(node.key, node.value)

                # Check if there is a next node (list)
                node = node.next

if __name__ == "__main__":
    ht = HashTable(2)

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
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")