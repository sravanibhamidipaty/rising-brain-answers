from collections import deque

"""
Intuition
The core challenge is reversing the First-In-First-Out (FIFO) nature of a queue to mimic the Last-In-First-Out (LIFO) nature of a stack. To make the most recent element reside at the "front" of the queue, every time we add a new element, we must rotate the queue so that the new element becomes the first item to be removed.

Approach (One Queue Design)
    1. Initialize: Use a single deque but strictly treat it as a queue (only use append and popleft).
    2. Push: Add the element x to the back of the queue.
        - Get the current size of the queue (let's call it n).
        - Rotate the first n-1 elements by popping them from the front and appending them back to the rear one by one. This places x at the very front.
    3. Pop/Top: Since the "top" of our stack is always at the "front" of our queue, we simply return the front element.
    4. Empty: Check if the queue length is zero.

Complexity Analysis
Push:
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    - Reasoning: We must iterate through all existing elements to reposition the new one.

Pop:
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reasoning: The element is already at the front of the queue.

Top:
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reasoning: Simple index access at the front.

Empty:
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reasoning: Constant time check.
"""

class MyStackOneQueue:
    # LC: https://leetcode.com/problems/implement-stack-using-queues/
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate the queue to bring the newest element to the front
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Standard queue popleft() is used to simulate stack pop()
        return self.queue.popleft()

    def top(self) -> int:
        # The front of the queue is the top of the stack
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

"""
Intuition
This approach mimics how a stack actually behaves: you just "throw" the item on top (the back of the queue). However, when it's time to remove the "top" element, you realize it's trapped at the back of the queue. To get it, you have to move everything in front of it out of the way.

Approach (Two Queues)
    1. Push: Simply append the element to q1.
    2. Pop: Move all elements except the last one from q1 to q2.
        - The remaining element in q1 is your "top"--save it to return.
        - Swap q1 and q2 so q1 is ready for the next operation.
    3. Top: Similar to Pop, but you append the last element to q2 as well instead of discarding it.
"""


class MyStackTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Fast push
        self.q1.append(x)

    def pop(self) -> int:
        # Move everything except the last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last element is the stack top
        res = self.q1.popleft()

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        res = self.q1[0]  # Peek the last element

        # Move the last element to q2 to preserve it
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return not self.q1

from collections import deque


class myStack:
    # GFG: https://www.geeksforgeeks.org/problems/stack-using-queue/1
    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        # remove top element
        if not self.q:
            return
        return self.q.popleft()

    def top(self):
        # return top element
        if not self.q:
            return -1
        return self.q[0]

    def size(self):
        # return current size
        return len(self.q)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

solutionLCOneQueue = MyStackOneQueue()
resultsLCOneQueue = []
resultsLCOneQueue.append(solutionLCOneQueue.push(1))
resultsLCOneQueue.append(solutionLCOneQueue.push(2))
resultsLCOneQueue.append(solutionLCOneQueue.top())
resultsLCOneQueue.append(solutionLCOneQueue.pop())
resultsLCOneQueue.append(solutionLCOneQueue.empty())
print(f"LC One Queue Solution: {resultsLCOneQueue}")

solutionLCTwoQueues = MyStackTwoQueues()
resultsLCTwoQueue = []
resultsLCTwoQueue.append(solutionLCTwoQueues.push(1))
resultsLCTwoQueue.append(solutionLCTwoQueues.push(2))
resultsLCTwoQueue.append(solutionLCTwoQueues.top())
resultsLCTwoQueue.append(solutionLCTwoQueues.pop())
resultsLCTwoQueue.append(solutionLCTwoQueues.empty())
print(f"LC Two Queues Solution: {resultsLCTwoQueue}")

solutionGFG = MyStackTwoQueues()
resultsGFG = []
resultsGFG.append(solutionGFG.push(1))
resultsGFG.append(solutionGFG.push(2))
resultsGFG.append(solutionGFG.top())
resultsGFG.append(solutionGFG.pop())
resultsGFG.append(solutionGFG.empty())
print(f"GFG Solution: {resultsGFG}")
