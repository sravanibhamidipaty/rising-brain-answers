"""
At most one character, means a valid palindrome is still valid?
Can s be empty?
Can s be only one character?
What kind of characters in s? What to include and what not to include like spaces are there etc?

TC: O(n) where n is the number of characters in s
SC: O(1) because we are using two pointers and calling isValid at most twice
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/valid-palindrome-ii/
    def validPalindrome(self, s: str) -> bool:
        def isValid(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isValid(left + 1, right) or isValid(left, right - 1)
            left += 1
            right -= 1
        return True


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/palindrome-string0817/1
    def isPalindrome(self, s):
        # code here
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.isPalindrome("abba")}")
print(f"LC Solution: {solutionLC.validPalindrome("abca")}")