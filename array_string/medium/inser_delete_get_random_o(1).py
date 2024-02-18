import random

"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        index = self.hash_map[val]
        last_val = self.list[-1]
        self.list[index] = last_val
        self.hash_map[last_val] = index
        self.list.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


obj = RandomizedSet()
assert obj.insert(1) is True
assert obj.remove(2) is False
assert obj.insert(2) is True
assert obj.getRandom() in [1, 2]
assert obj.remove(1) is True
assert obj.insert(2) is False
assert obj.getRandom() in [1, 2]
