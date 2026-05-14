"""
Complexity Analysis
push(x)
    - Time Complexity: O(1)
    - Space Complexity: O(N)

pop()
    - Time Complexity: O(1)
    - Space Complexity: O(1)

peek()
    - Time Complexity: O(1)
    - Space Complexity: O(1)

getMax()
    - Time Complexity: O(1)
    - Space Complexity: O(1)

isEmpty()
    - Time Complexity: O(1)
    - Space Complexity: O(1)

Time (O(1)): Every operation (including getMax) is just a basic
list access or a single comparison during the push. There
are no loops or searches.
Space (O(N)): For every element x pushed, you are actually
storing a pair: (value, current_max).
    - If you push N elements and never pop, your stack
    will contain N tuples.
    - While this technically doubles the constant factor
    of memory used (Storing two integers instead of one), it
    remains linear O(N) in Big O notation.
"""


class SpecialStackOneStack:
    def __init__(self):
        # Define Stack
        self.stack = []
        self.max_stack = []

    def push(self, x):
        # Add an element to the top of Stack
        if self.stack:
            self.stack.append((x, max(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self):
        # Remove the top element from the Stack
        return self.stack.pop()[0]

    def peek(self):
        # Returns top element of Stack
        return self.stack[-1][0] if self.stack else -1

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def getMax(self):
        # Finds maximum element of Stack
        return self.stack[-1][1] if self.stack else -1


class SpecialStackTwoStacks:
    def __init__(self):
        # Define Stack
        self.stack = []
        self.max_stack = []

    def push(self, x):
        # Add an element to the top of Stack
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            if self.max_stack[-1] <= x:
                self.max_stack.append(x)
        self.stack.append(x)

    def pop(self):
        # Remove the top element from the Stack
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def peek(self):
        # Returns top element of Stack
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def getMax(self):
        # Finds maximum element of Stack
        return self.max_stack[-1] if self.max_stack else -1

specialStackOneStack = SpecialStackOneStack()
specialStackTwoStacks = SpecialStackTwoStacks()
resultOneStack = []
resultTwoStack = []

resultOneStack.append(specialStackOneStack.push(2))
resultOneStack.append(specialStackOneStack.push(3))
resultOneStack.append(specialStackOneStack.peek())
resultOneStack.append(specialStackOneStack.pop())
resultOneStack.append(specialStackOneStack.getMax())
resultOneStack.append(specialStackOneStack.push(1))
resultOneStack.append(specialStackOneStack.getMax())
print(f"GFG One Stack Solution {resultOneStack}")

resultTwoStack.append(specialStackTwoStacks.push(2))
resultTwoStack.append(specialStackTwoStacks.push(3))
resultTwoStack.append(specialStackTwoStacks.peek())
resultTwoStack.append(specialStackTwoStacks.pop())
resultTwoStack.append(specialStackTwoStacks.getMax())
resultTwoStack.append(specialStackTwoStacks.push(1))
resultTwoStack.append(specialStackTwoStacks.getMax())
print(f"GFG One Stack Solution {resultTwoStack}")