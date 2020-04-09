class DynamicArray:
    def __init__(self, capacity = 8):
        self.length = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def insert(self, index, value):
        if self.length >= self.capacity:
            self.resize()

        # shift everything to the right of index, to the right
        for i in range(self.length, index, -1):
            self.storage[i] = self.storage[i - 1]
        # insert the value, at the index
        self.storage[index] = value
        self.length += 1
    
    def append(self, value):
        if self.length >= self.capacity:
            self.resize()
        self.storage[self.length] = value
        self.length += 1
    
    def resize(self):
        # create a new array, bigger in size
        self.capacity *= 2 # double the array size
        new_storage = [None] * self.capacity
        # move all elements from old array, into new one
        for i in range(self.length):
            new_storage[i] = self.storage[i]
        # set the new array to storage
        self.storage = new_storage