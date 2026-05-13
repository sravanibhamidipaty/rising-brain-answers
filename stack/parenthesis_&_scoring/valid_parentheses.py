"""
Can s be empty?
Can s contain other characters that is not parentheses?

TC: O(n) where n is the number of characters in the string
SC: O(n) + O(3) n is the number of characters in the string especially open parentheses if all of
them are open then n in the worst case O(3) for character_map which overall ends up being O(n)
"""


class Solution:
    # LC: https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        character_map = {"}": "{", "]": "[", ")": "("}
        stack = []

        for char in s:
            if char in character_map:
                if not stack or stack[-1] != character_map[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

    def isBalanced(self, s):
        # GFG: https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1
        # code here
        if not s:
            return True

        stack = []
        character_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in character_map:
                if not stack or stack[-1] != character_map[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

solution = Solution()
print(f"LC Solution: {solution.isValid("[{()}]")}")
print(f"GFG Solution: {solution.isBalanced("[{()}]")}")