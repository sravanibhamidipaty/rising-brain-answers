"""
Intuition
To delete an element in the middle of a stack, we must first
"get it out of the way" by removing all elements above it.
However, a stack is Last-In, First-Out (LIFO). If we simply
pop() elements to reach the middle, we lose the top half of
our data. The "aha!" moment is realizing that Recursion
allows us to store those popped elements in the function's
stack frame. ONce we reach the target middle element and
delete it, the recursion unwinds, and we push those stored
elements back onto the stack in their original order.

Approach (Recursive)
1. Calculate the target index: The problem defines the middle as
floor((size + 1) / 2) from the bottom.
2. Base Case: If we have reached the target position (counting
down from the top), we pop() the element and return without
pushing it back.
3. Recursive Step: pop() the current top element
and store it in a local variable.
    - Make a recursive call to reach the next depth (closer
    to the middle).
    - Once the recursive call returns (meaning the middle
    has been deleted), push() the stored local variable back
    onto the stack.

Complexity Analysis
Time Complexity: O(N)
    - We visit each element above the middle exactly once
    during the descent (popping) and once during the ascent (pushing).
    - In the worst case (middle is near the bottom), we process
    N/2 elements.
    - O(N/2) simplifies to O(N).

Space Complexity:O(N)
    - The problem states "without using any additional data structure",
    which usually refers to explicit structures like Arrays or
    HashMaps.
    - However, we use the Recursive Call Stack. Each recursive
    call adds a frame to the stack memory.
    - Since we recurse approximately N/2 times, the space complexity
    is O(N).

Dry Run:
    Initial Stack: [10, 20, 30, 40, 50] (Top is 50)
    Size (N): 5
    Target (from bottom): floor(5+1)/2 = 3 (The element 30)
    Elements to skip from top (count): 5 - 3 = 2

Execution Trace
Step    Function Call       Action              temp (Stored)
1       solve(stack, 2)     count>0, pop 50         50
2       solve(stack, 1)     count>0, pop 40         40
3       solve(stack, 0)     count==0, pop 30        return
4       Return to step 2    Push temp (40)          40
5       Return to step 1    Push temp (50)          50
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1
    def deleteMid(self, stack):
        # target is the 1-based index from the bottom
        # we convert this to "how many elements to pop from
        # top"
        target_from_bottom = (len(stack) + 1) // 2

        # We need to skip (len(stack)-target_from_bottom) elements
        self.solve(stack, len(stack) - target_from_bottom)

    def solve(self, s, count):
        # Base Case: We have skipped the required elements,
        # the current top is the middle element.
        if count == 0:
            stack.pop()
            return

        # Recursive Step:
        # 1. Remove the top element
        temp = s.pop()

        # 2. Recurse to reach the middle element
        self.solve(stack, count - 1)

        # Backtrack: Put the element back
        stack.append(temp)
