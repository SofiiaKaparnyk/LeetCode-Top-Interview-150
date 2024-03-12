"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
 If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""


class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


# SOLUTION 1 - TOO  LONG
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = None
#         self.tail = self.head
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.move_to_end(key)
#         return self.cache.get(key, -1)
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.head = self.move_to_end(key)
#
#         else:
#             if not self.head:
#                 self.head = ListNode(key)
#                 self.tail = self.head
#             else:
#                 new_node = ListNode(key)
#                 self.tail.next = new_node
#                 new_node.prev = self.tail
#                 self.tail = new_node
#
#         self.cache[key] = value
#
#         if len(self.cache) > self.capacity:
#             del self.cache[self.head.val]
#             self.head = self.head.next
#             self.head.prev = None
#
#     def move_to_end(self, key):
#         if key == self.tail.val:
#             return self.head
#
#         curr = self.head
#         while curr:
#             if curr.val == key:
#                 if curr.prev:
#                     curr.prev.next = curr.next
#                     curr.next.prev = curr.prev
#                 else:
#                     if self.head.next:
#                         self.head = self.head.next
#                         self.head.prev = None
#
#                 curr.next = None
#                 self.tail.next = curr
#                 curr.prev = self.tail
#                 self.tail = curr
#                 break
#
#             curr = curr.next
#         return self.head


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()  # Dummy head
        self.tail = ListNode()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_end(node)

        else:
            new_node = ListNode(key, value)
            self.add_to_end(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                del self.cache[self.head.next.key]
                self.remove_node(self.head.next)

    def move_to_end(self, node):
        self.remove_node(node)
        self.add_to_end(node)

    def add_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # Output: 1
# cache.put(3, 3)
# print(cache.get(2))  # Output: -1
# cache.put(4, 4)
# print(cache.get(1))  # Output: -1
# print(cache.get(3))  # Output: 3
# print(cache.get(4))  # Output: 4


# cache = LRUCache(2)
# cache.put(2, 1)
# cache.put(2, 2)
# print(cache.get(2))  # Output: 2
# cache.put(1, 1)
# cache.put(4, 1)
# print(cache.get(2))  # Output: -1


# cache = LRUCache(2)
# print(cache.get(2))  # Output: -1
# cache.put(2, 6)
# print(cache.get(1))  # Output: -1
# cache.put(1, 5)
# cache.put(1, 2)
# print(cache.get(1))  # Output: 2
# print(cache.get(2))  # Output: 6

# cache = LRUCache(3)
# cache.put(2, 1)
# cache.put(1, 1)
# cache.put(2, 3)
# cache.put(4, 1)
# print(cache.get(1)) # 1
# print(cache.get(1)) # 1
# cache.put(5, 2)
# print(cache.get(2)) # -1
# cache.put(7, 2)
# print(cache.get(2)) # -1
# print(cache.get(5)) # 2
# print(cache.get(1))  # Output: 1
# print(cache.get(2))  # Output: -1

cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
print(cache.get(4))  # 4
print(cache.get(3))  # 3
print(cache.get(2))  # 2
print(cache.get(1))  # -1
cache.put(5, 5)
print(cache.get(1))  # -1
print(cache.get(2))  # 2
print(cache.get(3))  # 3
print(cache.get(4))  # -1
print(cache.get(5))  # 5
