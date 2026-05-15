"""
Intuition
The problem asks to print 1 to N, but in recursion,
the easiset way to break the problem down is to look at N
first.
    - If we print N immediately, we get a descending order
    (5, 4, 3, 2, 1).
    - To get ascending order (1, 2, 3, 4, 5), we must postpone
    the printing.
    - We "suspend" the current number, move to the next smaller
    number, and only print once the smaller numbers have
    finished their work.

Approach: Head Recursion
The Head Recursion strategy involves making the recursive
call before performing the action (printing).
    1. Base Case: If N is less than 1, return immediately
    (nothing to print).
    2. Recursive Step: Call printTillN(N-1). This goes all
    the way down to 1.
    3. The Action: Print N. Because of the way the stack
    works, the function call for N = 1 finishes its recursive
    step first, prints 1, and then returns control to N = 2,
    which then prints 2, and so on.

Time Complexity
The time complexity is O(N).
Each number from 1 to N is visited exactly once. We perform
a constant amount of work (a comparison and a print statement)
for each of the N recursive calls.

Space Complexity
The space complexity is O(N).
Even though we aren't using an explicit data structure like
a list, each recursive call adds a stack frame to the memory.
Since we recurse N times before reaching the base case, there
will be N frames on the call stack at the deepest point
of recursion.
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1
    def printTillN(self, N):
        # code here
        # 1. Base Case: The stopping condition
        if N < 1:
            return

        # 2. Recurisve Call: Wind up the stack until we reach 1
        self.printTillN(N - 1)

        # 3. Action: Print N as the stack unwinds
        print(N, end=" ")

solution = Solution()
solution.printTillN(5)