"""
Intuition
The core idea is to use two stacks to reverse the order of elements twice.
Since a stack is Last-In-First-Out (LIFO), pushing elements into one
stack and then popping into another reverses their order,
effectively creating a First-In-First-Out (FIFO) sequence.
We designate stack1 as the input (where all new elements land) and stack2
as the output (where we serve peek/pop requests). We only move elements
from input to output when the output stack is empty.

Approach
    - Push: Always append the element to stack1. This is a simple O(1) operation.
    - Pop/Peek: 1. Check if stack2 is empty. 2. If it is, "pour" everything
    from stack1 into stack2 using a loop. This reverses the order so the
    oldest element is now on top of stack2. 3. Perform the pop/peek operation on stack2.
    - Empty: The queue is empty only if both stacks are empty.

Time Complexity
    - Push O(1) per operation.
    - Pop/Peek: Amortized O(1).
        - While a single pop might trigger an O(N) move if stack2 is empty,
        each element is pushed into stack1 once, popped from stack1 once,
        pushed into stack2 once, and popped from stack2 once. This results in a
        total of 4 operations per element over its entire life in the queue, regardless
        of how many pops occur.
    - Empty: O(1)

Space Complexity
    - O(N), where N is the number of elements currently stored in the queue.
    We are using two stacks to store the total number of elements.
"""

class MyQueue:
    # LC: https://leetcode.com/problems/implement-queue-using-stacks/
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

class myQueue:
    # GFG: https://www.geeksforgeeks.org/problems/queue-using-stack/1
    def __init__(self):
        # Initialize your data members
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        # Implement the enqueue operation
        self.stack1.append(x)

    def dequeue(self):
        # Implement the dequeue operation
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1

    def front(self):
        # Return the front element of the queue
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else -1

    def size(self):
        # Return the current size of the queue
        return len(self.stack1) + len(self.stack2)

solutionLC = MyQueue()
resultLC = []
resultLC.append(solutionLC.push(1))
resultLC.append(solutionLC.push(2))
resultLC.append(solutionLC.peek())
resultLC.append(solutionLC.pop())
resultLC.append(solutionLC.empty())
print(f"LC Solution: {resultLC}")

solutionGFG = myQueue()
resultGFG = []
resultGFG.append(solutionGFG.enqueue(5))
resultGFG.append(solutionGFG.enqueue(3))
resultGFG.append(solutionGFG.enqueue(4))
resultGFG.append(solutionGFG.front())
resultGFG.append(solutionGFG.dequeue())
resultGFG.append(solutionGFG.size())
resultGFG.append(solutionGFG.front())
print(f"GFG Solution: {resultGFG}")

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()