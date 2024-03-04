"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

"""


class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        if not self.min_stack or (self.min_stack and val <= self.min_stack[-1]):
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        last = self.stack.pop()
        if self.min_stack[-1] == last:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


obj = MinStack()
assert obj.push(0) is None
assert obj.push(-2) is None
assert obj.push(0) is None
assert obj.push(-3) is None
assert obj.getMin() == -3
assert obj.pop() is None
assert obj.pop() is None
assert obj.pop() is None
assert obj.top() == 0
assert obj.getMin() == 0

obj = MinStack()
assert obj.push(0) is None
assert obj.push(1) is None
assert obj.push(0) is None
assert obj.getMin() == 0
assert obj.pop() is None
assert obj.getMin() == 0

obj = MinStack()
assert obj.push(2147483646) is None
assert obj.push(2147483646) is None
assert obj.push(2147483647) is None
assert obj.top() == 2147483647
assert obj.pop() is None
assert obj.getMin() == 2147483646
assert obj.pop() is None
assert obj.getMin() == 2147483646
assert obj.pop() is None
assert obj.push(2147483647) is None
assert obj.top() == 2147483647
assert obj.getMin() == 2147483647
