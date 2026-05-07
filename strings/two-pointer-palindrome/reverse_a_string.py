"""
TC: O(n) where n is the length of s
SC: O(n)  where n is the length of s
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/reverse-a-string/1
    # LC: https://leetcode.com/problems/reverse-string/description/
    def reverseString(self, s: str) -> str:
        # code here
        left = 0
        right = len(s) - 1

        result = list(s)

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return "".join(result)
