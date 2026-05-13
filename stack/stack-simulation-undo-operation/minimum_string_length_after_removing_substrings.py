"""
Time Complexity: O(n)
    - You are peforming a single pass through the string s.
    - Each character is pushed onto the stack once and popped at most once. Since stack operations (push and pop) are O(1), the overall time scales linearly with the length of the string.

Space Complexity: O(n)
    - In the worst-case scenario (e.g., a string like "XYZ"), no characters are removed, and the stack grows to the size of the input string s.
"""
class Solution:
    # LC: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack and ((stack[-1] == "A" and char == "B") or (stack[-1]=="C" and char=="D")):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)

solution = Solution()
print(f"LC Solution: {solution.minLength("ABFCACDB")}")