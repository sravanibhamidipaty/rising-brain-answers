"""
Time Complexity: O(n)
    - You are iterating through the string s exactly once. Each character involves a constant time O(1) operation (either incrementing or decrementing a counter).

Space Complexity: O(1)
    - Regardless of how large the input string s is, you only ever store two integer variables (open_brackets and minimum_to_add). This is often referred to as constant space.
"""


class Solution:
    # LC: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        minimum_to_add = 0

        if not s:
            return 0

        for char in s:
            if char == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    minimum_to_add += 1

        return minimum_to_add + open_brackets

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

solution = Solution()
print(f"LC Solution: {solution.minAddToMakeValid("(()(")}")
print(f"GFG Solution: {solution.minParentheses("(()(")}")