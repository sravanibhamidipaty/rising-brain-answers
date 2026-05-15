"""
Intuition
1. Empty the Stack: We pop everything off and "hold" those values
in the recursion memory until the stack is empty.
2. The Trick: Once the stack is empty, we don't just push
the elements back. We need a helper function that inserts each
element at the bottom of the stack instead of the top.

The Approach: Double Recursion
We use two recursive functions:
    - reverseStack: Pops an element and calls itself until
    the stack is empty, then calls insertAtBottom.
    - insertAtBottom: Pushes an element to the very bottom
    by popping everything else out first, placing the target,
    and then putting the popped elements back.

Complexity Analysis
Time Complexity: O(N^2)
    - We iterate through N elements in reverseStack, and
    for each element, we call insertAtBottom, which also
    takes O(N) time.

Space Complexity: O(N)
    - No extra data structures are used, but the recursion
    stack (internal memory) goes N levels deep.
"""


class SolutionBruteForce:
    # GFG: https://www.geeksforgeeks.org/problems/reverse-a-stack/1#approach-1-using-recursion
    def reverseStack(self, st):
        # code here
        if not st:
            return

        # 1. Pop the element
        temp = st.pop()

        # 2. Reverse the remaining stack
        self.reverseStack(st)

        # 3. Insert the popped element at the bottom
        self.insertAtBottom(st, temp)

        return st

    def insertAtBottom(self, st, element):
        # Base case: if stack is empty, just push the element
        if not st:
            st.append(element)
            return

        # Pop everything to reach the bottom
        temp = st.pop()
        self.insertAtBottom(st, element)

        # Push the popped items back on top
        st.append(temp)

class SolutionOptimal:
    def reverseStack(self, stack):
        aux = []

        # move all elements to auxiliary stack
        while stack:
            aux.append(stack.pop())

        # replace original stack with auxiliary stack
        stack[:] = aux
        return stack

solutionBruteForce = SolutionBruteForce()
solutionOptimal = SolutionOptimal()
print(f"GFG Solution Brute Force: {solutionBruteForce.reverseStack([1, 2, 3, 4, 5])}")
print(f"GFG Solution Optimal: {solutionOptimal.reverseStack([1, 2, 3, 4, 5])}")