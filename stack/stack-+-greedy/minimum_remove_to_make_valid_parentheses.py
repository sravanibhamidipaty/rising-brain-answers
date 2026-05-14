"""
Questions:
Can the string contain no parentheses?
Can the string only contain parentheses?
Can the string be empty?

TC: O(n) where n is the number of characters in the string
SC: O(n) where n is the number of characters in the string in worst case if all parentheses are valid.
It is probably O(2n), but the bucket is still O(n)
"""


class SolutionLCBruteForce:
    # LC: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        open_count = 0
        stack = []

        for char in s:
            if char == ")" and open_count == 0:
                continue
            if char == "(":
                open_count += 1
            elif char == ")":
                open_count -= 1
            stack.append(char)

        close_count = 0
        result = []

        for char in reversed(stack):
            if char == "(" and close_count == 0:
                continue
            if char == ")":
                close_count += 1
            elif char == "(":
                close_count -= 1
            result.append(char)

        return "".join(result[::-1])

"""
Intuition
A string is valid if, at any point during a left-to-right scan, the number of closing parentheses never exceeds the number of opening ones, and the totals match at the end.
    - The "Immediate" Problem: If we see a ) and having no matching ( to pair it with, that ) is definitively invalid. We can mark it for removal immediately.
    - The "Delayed" Problem: If we reach the end of the string and still have "leftover" ( that were never closed, those are also invalid. However, since any of the ( could have been the "extra" one, we usually store their indices to know exactly which ones to remove later.

Approach: Stack + Marker
We use a Stack to keep track of the indices of opening parentheses.
    1. Iterate through the string:
        - If we see a (: Push its index onto the stack.
        - If we see a ):
            - If the stack is not empty, pop() (we found a valid pair).
            - If the stack is empty, this ) is invalid. Replace it with a placeholder like "" or a special character) or its index in a set.
    2. Post-Process: After the loop, any indices remaining in the stack represent ( that never found a match. Mark these for removal as well.
    3. Reconstruct: Build the final string by joining all characters that weren't marked.

Time Complexity: O(n)
    - We traverse the string once (O(n)).
    - Stack operations (push/pop) are O(1).
    - The final "".join(s) operation is O(n).
    - Since these are sequential, the overall complexity remains linear relative to the length of the string.

Space Complexity: O(n)
    - Stack: In the worst case (e.g., "((((("), the stack stores n indicies, leading to O(n) space.
    - String Conversion: Since strings in Python are immutable, converting the string to a list to perform in-place removals (or building a new list) requires O(n) space.
"""

class SolutionLCOptimal:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)

        stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            if char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""  # Mark extra ")"

        # Mark remaining '(' in stack for removal
        while stack:
            s[stack.pop()] = ""

        return "".join(s)

"""
Time Complexity: O(n)
- You are performing a single pass through the string s. Each
character is visited exactly once, and the operations inside
the loop (incrementing/decrementing counters) are all O(1).

Space Complexity: O(1)
- Unlike the common "Stack" approach for parentheses problems 
which requires O(n) space, you are only using two integer variables
(min_to_add and open_count). The memory usage remains constant
regardless of the input size.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/min-add-to-make-parentheses-valid/1
    def minParentheses(self, s):
        # code here

        min_to_add = 0
        open_count = 0

        for char in s:
            if char == "(":
                open_count += 1
            elif char == ")":
                if open_count > 0:
                    open_count -= 1
                else:
                    min_to_add += 1
        return min_to_add + open_count

solutionLCBruteForce = SolutionLCBruteForce()
solutionLCOptimal = SolutionLCOptimal()
solutionGFG = SolutionGFG()

print(f"LC Solution Brute Force: {solutionLCBruteForce.minRemoveToMakeValid("lee(t(c)o)de)")}")
print(f"LC Solution Optimal: {solutionLCBruteForce.minRemoveToMakeValid("lee(t(c)o)de)")}")
print(f"GFG Solution: {solutionGFG.minParentheses("(()(")}")