"""
Intuition
The core challenge is handling the nesting: (A) is 2 x A. This means every time we see a (, we are entering a deeper "level" of score multiplication. When we see (), we've found a "core" value of 1, but its actual contribution depends on how many layers of parentheses wrap around it.
For example, in (()()):
    - The first () is at depth 1, so it contributes 2**1.
    - The second is also at depth 1, so it contributes 2**1.
    - Total = 2 + 2 = 4.

Approach: The Stack Method
We use a stack to keep track of the "running total" at each nesting level.
    1. Initialize a stack with a single 0. This represents the score at the current outermost level.
    2. Iterate through the string:
        - If you see (: Start a new level by pushing a 0 onto the stack.
        - If you see ): Finish the current level: Pop the last score (let's call it inner_score).
            - The value of this level is max(2*inner_score, 1).
            - Add this value to the new top of the stack (the parent level).
    3. Return the only value left in the stack.

Time Complexity: O(n)
We iterate through the string s exactly once. Each character is pushed and popped from the stack at most once.

Space Complexity: O(n)
In the worst case (a string like ((((()))))), the stack will grow to a size of n/2.
"""


class SolutionLCStack:
    # LC: https://leetcode.com/problems/score-of-parentheses/
    def scoreOfParentheses(self, s: str) -> int:
        # Stack stores the score of the current 'level'
        stack = [0]

        for char in s:
            if char == "(":
                # Move to a deeper level
                stack.append(0)
            else:
                # Pop the score of the inner component
                inner_score = stack.pop()
                # If inner_score is 0, it was "()", so score is 1
                # Otherwise, it was "(A)", so score is 2*A
                current_val = max(2 * inner_score, 1)

                # Add the calculated score to the previos level
                stack[-1] += current_val

        return stack[0]

"""
Intuition
In the string ((())), the inner () is at depth 2 (if we start counting from 0).
    - Depth 0: (
    - Depth 1: (
    - Depth 2: ()

Each depth level represents a multiplief of 2. So, a () at depth d contributes 2**d to the total score. We only care about the "innermost" pairs because those are the only ones that provide the base value of 1; every other set of parentheses just doubles what's inside.

Approach: Counting Layers
We maintain a running depth and a total_score.
    1. Traverse the string.
    2. If you encounter (: Increment depth.
    3. If you encounter ):
        - Check if the previous character was (.
        - If yes, we've found a leaf pair (). Add 2**(depth-1) to the total score.
        - Decrement the depth (regardless of whether it was a leaf).

Time Complexity: O(n)
    - We still visit every character in the string s once.

Space Complexity: O(1)
    - We only store two integer variables (total_score and depth), regardless of the input size.
"""


class SolutionOptimal:
    def scoreOfParentheses(self, s: str) -> int:
        total_score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                # Check if this ")" is closing a "()" pair
                if s[i - 1] == "(":
                    # bitwise shift 1 << depth is equivalent to 2^depth
                    total_score += 1 << depth

        return total_score

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/score-of-parentheses-string/1
    def scoreOfParentheses(self, s):
        # code here
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                inner_score = stack.pop()
                current_val = max(2 * inner_score, 1)
                stack[-1] += current_val
        return stack[0]


solutionLCStack = SolutionLCStack()
solutionOptimal = SolutionOptimal()
solutionGFG = SolutionGFG()
print(f"LC Solution Stack: {solutionLCStack.scoreOfParentheses("(())")}")
print(f"LC Solution Optimal: {solutionLCStack.scoreOfParentheses("(())")}")
print(f"GFG Solution: {solutionGFG.scoreOfParentheses("(())")}")