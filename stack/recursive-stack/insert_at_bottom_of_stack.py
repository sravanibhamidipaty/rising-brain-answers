"""
Time Complexity: O(n), where n is the number of elements in
the stack. We visit each element once.

Space Complexity: O(n) due to the Recursive Call Stack.
Interviewers will specifically ask you about this; even though
you aren't using an extra list, the memory used by the
recursion counts as auxiliary space.
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1
    def insertAtBottom(self, st, x):
        # code here
        # Base Case: If stack is empty, insert x at the bottom
        if not st:
            st.append(x)
            return st

        # Recursive Step:
        # 1. Pop the top element
        temp = st.pop()

        # 2. Recurse to reach the bottom
        self.insertAtBottom(st, x)

        # 3. Push the element back after x has been inserted
        # at the bottom
        st.append(temp)

        return st

solution = Solution()
print(f"GFG Solution: {solution.insertAtBottom([4,3,2,1,8], 2)}")