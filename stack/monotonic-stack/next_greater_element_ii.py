from typing import List

"""
Intuition
The core of this problem is identifying the first element to the right
that is strictly larger than the current one.
    - The "Waiting Room" Analogy: Imagine a line of people. Each person is looking for someone taller than them to their right. If you haven't found your "taller person" yet, you stay in a "waiting room" (the Stack).
    - The Monotonic Property: Because we want the next greater element, we only care about people in stack who are shorter than the new comer. As soon as a "tall person" (new element) arrives, they "resolve" everyone in the stack who is shorter than them.
    - The Circular Twist: Since the array wraps around, a person at the end of the line might find their "taller person" at the very beginning. To simulate this without actually duplicating the array in memory, we conceptually iterate through the array twice (2n).

The Approach: Monotonic Stack
This is the most efficient way to handle "next greater/smaller" problems.
    1. Initialize: Create a result array res filled with -1. Use a stack to store indices (not values) of elements we haven't found a match for yet.
    2. The 2n Loop: Iterate from i = 0 to 2n - 1. Use idx = i % n to wrap around the array indices.
    3. The Resolution Step (While Loop): While the stack is not empty AND the current element nums[idx] is greater than the element at the index on top of the stack (nums[stack.top()]):
        - We've found the "Next Greater Element for the index at the top of the stack.
        - Pop the index and set the result at the index to this number.
    4. The Push Step: Only push indices onto the stack during the first pass (i < n). By the second pass, we are only there to resolve any remaining indices left over from the first pass.

Time Complexity: O(n)
    - The "Push-Pop" Rule: Even though we have a while loop inside a for loop, each index is pushed onto the stack exactly once (during the first pass) and popped at most once.
    - Total operations are operational to 2n (for the loops) + n for stack operations, which simplifies to O(n).

Space Complexity: O(n)
    - Result Array: We need O(n) space to store the output.
    - The Stack: In the worst-case scenario (e.g., a strictly decreasing array like [5, 4, 3, 2, 1]), the stack will hold n indicies before any are popped. Thus O(n).
"""


class Solution:
    # LC: https://leetcode.com/problems/next-greater-element-ii/
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Monotonic decreasing stack

        # Conceptually concatenate the array with itself
        for i in range(2 * n):
            idx = i % n

            # Resolve elements in stack smaller than current value
            while stack and nums[idx] > nums[stack[-1]]:
                res[stack.pop()] = nums[idx]

            # Only add to stack during the first pass
            if i < n:
                stack.append(idx)
        return res

solution = Solution()
print(f"LC Solution: {solution.nextGreaterElements([1,2,1])}")