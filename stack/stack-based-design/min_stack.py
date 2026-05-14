"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

This docstring covers two "FAANG-style" implementation strategies:
1. One-Stack (Tuple Approach): Stores (value, current_min) in a single list.
2. Two-Stack (Optimized Approach): Stores values in one list and
   only new minimums in a second list.

--- APPROACH 1: ONE STACK (Tuple-based) ---
Pros: Highly readable, less logic for edge cases, less prone to bugs.
Cons: Higher memory usage because a 'minimum' is stored for every entry.
Space Complexity: O(n) - specifically 2n storage.

--- APPROACH 2: TWO STACKS (Memory-optimized) ---
Pros: Better average-case memory usage. If you push many values larger than
      the current minimum, the 'min_stack' does not grow.
Cons: Slightly more conditional logic in push/pop operations.
Space Complexity: O(n) - worst case 2n, but often much closer to 1n.

Complexity Analysis (Both Approaches):
    - Time: O(1) for all operations (push, pop, top, getMin).
    - Space: O(n) to store the elements.
"""

class MinStackOneStack:
    # LC: https://leetcode.com/problems/min-stack/
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStackTwoStack:

    def __init__(self):
        """
        Initializes the stack object.
        Note: The implementation below follows the Two-Stack strategy.
        """
        self.stack = []  # Primary stack for all values
        self.min_stack = []  # Auxiliary stack for tracking minimums

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.

        Logic: Always push to main stack. Only push to min_stack if the
        new value is <= the current minimum (or if it's the first element).
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.

        Logic: If the value being removed is the same as the current
        minimum, remove it from the min_stack as well.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack."""
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack in O(1)."""
        return self.min_stack[-1] if self.min_stack else None

class SpecialStack:
    # GFG: https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
    def __init__(self):
        # Define Stack
        self.stack = []

    def push(self, x):
        # Add an element to the top of Stack
        if not self.stack:
            self.stack.append([x, x])
        else:
            self.stack.append([x, min(self.stack[-1][1], x)])

    def pop(self):
        # Remove the top element from the Stack
        return self.stack.pop()[0]

    def peek(self):
        # Returns top element of Stack
        return self.stack[-1][0] if self.stack else -1

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def getMin(self):
        # Finds minimum element of Stack
        return self.stack[-1][1] if self.stack else -1


minStackLCOneStack = MinStackOneStack()
minStackLCTwoStack = MinStackTwoStack()
solutionGFG = SpecialStack()
resultLCTwoStack = []
resultLCOneStack = []
resultGFG = []
resultLCOneStack.append(minStackLCOneStack.push(-2))
resultLCOneStack.append(minStackLCOneStack.push(0))
resultLCOneStack.append(minStackLCOneStack.push(-3))
resultLCOneStack.append(minStackLCOneStack.getMin())
resultLCOneStack.append(minStackLCOneStack.pop())
resultLCOneStack.append(minStackLCOneStack.top())
resultLCOneStack.append(minStackLCOneStack.getMin())
print(f"LC Solution One Stack: {resultLCOneStack}")

resultLCTwoStack.append(minStackLCTwoStack.push(-2))
resultLCTwoStack.append(minStackLCTwoStack.push(0))
resultLCTwoStack.append(minStackLCTwoStack.push(-3))
resultLCTwoStack.append(minStackLCTwoStack.getMin())
resultLCTwoStack.append(minStackLCTwoStack.pop())
resultLCTwoStack.append(minStackLCTwoStack.top())
resultLCTwoStack.append(minStackLCTwoStack.getMin())
print(f"LC Solution Two Stack: {resultLCTwoStack}")

resultGFG.append(solutionGFG.push(-2))
resultGFG.append(solutionGFG.push(0))
resultGFG.append(solutionGFG.push(-3))
resultGFG.append(solutionGFG.getMin())
resultGFG.append(solutionGFG.pop())
resultGFG.append(solutionGFG.peek())
resultGFG.append(solutionGFG.getMin())
resultGFG.append(solutionGFG.isEmpty())
print(f"GFG Solution: {resultGFG}")