"""
Time Complexity: O(n)
Space Complexity: O(n) due to stack overflow
"""


class SolutionRecursive:
    # GFG: https://www.geeksforgeeks.org/problems/factorial5739/1
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


"""
Intuition
The factorial of a non-negative integer n (denoted as n!)
is the product of all positive integers less than or equal
to n.
    - Base Case: By definition, 0! = 1.
    - Recursive Structure: We can observe that 5! = 5x(4x3x2x1),
    which is the same as 5x4!. This gives us the recurrence
    relation: f(n) = n x f(n-1)

Approach
While the problem can be solved recursively, an interative approach
is usually preferred in production environments to avoid "Stack
Overflow" errors for large n. However, given the constraints
(0<=n<=12), both methods are safe.

Iterative Implementation (Recommended)
    1. Initialize a variable res to 1.
    2. Loop from 2 up to n.
    3. In each iteration, multiply res by the current number.
    4. Return res.

Recursive Implementation
    1. Base Case: If n is 0 or 1, return 1.
    2. Recursive Step: Return n x factorial(n-1).

Complexity Analysis
Time Complexity: O(n)
We perform exactly n multiplications to reach the result. Whether
using a for loop or n recursive calls, the work scales linearly
with the input n.

Space Complexity:
    Iterative: O(1)
    We only use a single variable to store the product, regardless
    of how large n is.

    Recursive: O(n)
    Each recursive call adds a new layer to the call stack. For
    n = 12, there will be 12 hidden stack frames in memory until
    the base case is reached.
"""

class SolutionIterative:
    def factorial(self, n: int) -> int:
        # Iterative approach for O(1) space
        res = 1

        for i in range(2, n+1):
            res *= i

        return res

solutionRecursive = SolutionRecursive()
solutionIterative = SolutionIterative()

print(f"GFG Recursive Solution: {solutionRecursive.factorial(5)}")
print(f"GFG Iterative Solution: {solutionIterative.factorial(5)}")