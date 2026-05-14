"""
Complexity Analysis

__init__(maxSize)
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reason: Just initializes variables. No elements stored yet.

push(x)
    - Time Complexity: O(1) amortized
    - Space Complexity: O(1) auxiliary
    - Reason: append() in Python lists is amortized constant time. The function itself does not create extra space proportional to n. The stack as a whole can grow to O(n) space overall, but the operation uses O(1) extra space.

pop()
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reason: list.pop() from the end is constant time. No extra memory used.

increment(k, val)
    - Time Complexity: O(k)
    - Space Complexity: O(1)
    - Reason: The loop runs k times. No extra data structures are created.
"""


class CustomStackLCBruteForce:
    # LC: https://leetcode.com/problems/design-a-stack-with-increment-operation/
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))

        for i in range(k):
            self.stack[i] += val


"""
Intuition
The bottleneck in the basic approach is the eager update. We can optimize by being "lazy"--only applying the increment when an element is actually leaving the stack (pop). By storing the increment at the highest index affected (k-1), we can ensure that as we pop elements, the increment "bleeds" down to the elements below it.

Approach
    - Maintain a stack for values and an inc array of the same size to store pending increments.
    - increment(k, val): Find the highest index that should be affected: idx = min(k, len(stack)) - 1. Add val to inc[idx].
    - pop():
        1. Target the top index: idx = len(stack) - 1.
        2. The actual value is stack[idx] + inc[idx].
        3. The Hand-off: If there's an element below (idx > 0), pass the current increment down: inc[idx-1] += inc[idx].
        4. Reset inc[idx] = 0 and return the result.

Complexity Analysis
    - Time Complexity: All operations (push, pop, increment) are now O(1). This is the theoretical limit for this problem.
    - Space Complexity: O(N) where N is maxSize. We use an additional array to track the increments, but this matches the space used by the stack itself.
"""


class CustomStackLCOptimal:
    # LC: https://leetcode.com/problems/design-a-stack-with-increment-operation/
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = [0] * maxSize
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        idx = len(self.stack) - 1
        # Calculate result with the 'lazy' increment
        res = self.stack.pop() + self.inc[idx]

        # Pass the increment down to the next element
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]

        # Clear the increment for this slot
        self.inc[idx] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            # Only increment up to what's actually in the stack
            idx = min(k, len(self.stack)) - 1
            self.inc[idx] += val

class myStackGFG:
    # GFG: https://www.geeksforgeeks.org/problems/stacks-operations/1
    # Define your stack
    def __init__(self):
        self.stack = []

    def push(self, x):
        # insert x into stack
        self.stack.append(x)

    def pop(self):
        # remove top ele from stack
        return self.stack.pop()

    def peek(self):
        # return top of stack
        return self.stack[-1]

    def getSize(self):
        # return current size of stack
        return len(self.stack)

    def isEmpty(self):
        # check whether stack is empty
        return len(self.stack) == 0


customStackLCBruteForce = CustomStackLCBruteForce(3)
resultLCBruteForce = []
resultLCBruteForce.append(customStackLCBruteForce.push(1))
resultLCBruteForce.append(customStackLCBruteForce.push(2))
resultLCBruteForce.append(customStackLCBruteForce.push(3))
resultLCBruteForce.append(customStackLCBruteForce.pop())
resultLCBruteForce.append(customStackLCBruteForce.increment(1, 100))
print(f"LC Solution Brute Force: {resultLCBruteForce}")

customStackLCOptimal = CustomStackLCOptimal(3)
resultLCOptimal = []
resultLCOptimal.append(customStackLCOptimal.push(1))
resultLCOptimal.append(customStackLCOptimal.push(2))
resultLCOptimal.append(customStackLCOptimal.push(3))
resultLCOptimal.append(customStackLCOptimal.pop())
resultLCOptimal.append(customStackLCOptimal.increment(1, 100))
print(f"LC Solution Brute Force: {resultLCOptimal}")

myStack = myStackGFG()
resultGFG= []
resultGFG.append(myStack.push(1))
resultGFG.append(myStack.push(2))
resultGFG.append(myStack.push(3))
resultGFG.append(myStack.peek())
resultGFG.append(myStack.pop())
resultGFG.append(myStack.getSize())
resultGFG.append(myStack.isEmpty())
print(f"GFG Solution: {resultGFG}")