"""
Can the string be empty? If so is an empty string True?
Can the string have one character? If so is that a valid palindrome?
Can it contain special characters that I need consider or skip?

Time Complexity: O(n) in the bigger bucket although due to two pointers, it would be O(N/2) to be specific
Space Complexity: O(1) only 2 pointers are used not creating or storing anything anywhere
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/string-palindromic-ignoring-spaces4723/1
    def isPalinSent(self, s):
        # code here
        def isAlphaNumeric(char):
            return "a" <= char <= "z" or "0" <= char <= "9"

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not isAlphaNumeric(s[left].lower()):
                left += 1
            while left < right and not isAlphaNumeric(s[right].lower()):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    # LC: https://leetcode.com/problems/valid-palindrome/
    def isPalindrome(self, s: str) -> bool:
        def isValidCharacter(char):
            return "a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9"

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not isValidCharacter(s[left]):
                left += 1
            while left < right and not isValidCharacter(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

solution = Solution()
print(f"GFG Solution: {solution.isPalinSent("Too hot to hoot")}")
print(f"LC Solution: {solution.isPalindrome("Too hot to hoot")}")