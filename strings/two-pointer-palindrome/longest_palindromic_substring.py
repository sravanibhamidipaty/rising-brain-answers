"""
1. The Intuition
A palindrome reads the same forward and backward. The key insight is that a palindrome is mirrored around its center.
If you pick a character (or the gap between two characters) as a "center," you can expand outwards as long as the characters on the left and right match.
    - Odd-length characters: A single character (e.g., "aba", center is b).
    - Even-length characters: The gap between two identical characters (e.g., "abba", center is the gap between b and b).

2. The Approach
We iterate through the string and, for each index, treat it as a potential center for both odd and even palindromes.
    1. Initialize: Keep track of the start and end indices of the largest palindrome found so far.
    2. Iterate: Loop through the string from i = 0 to n - 1.
    3. Expand: For each i:
        - Expand outward assuming i is the center (odd: expand(i, i))
        - Expand outward assuming the gap between i and i+1 is the center (even: expand(i, i+1)).
    4. Update: If the current expansion is longer than our global maximum, update our indices.
    5. Return: Slice the string using the final indices.

Time Complexity: O(n^2)
    - We iterate through the string of length n exactly once.
    - For each center the expandAroundCenter function can take up to O(n) time in the worst case (e.g., the string "aaaaa").
    - Total time: n x O(n) = O(n^2)

Space Complexity: O(1)
    - Unlike Dynamic Programming approach--which requires an O(n^2) table to store states--this approach only uses a few integer variables (start, end, i, left, right). Note: Returning the final string takes O(n) space, but the auxiliar space used by the algorithm is constant.
"""

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
    def longestPalindrome(self, s):
        # code here
        start = 0
        end = 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i + 1)

            max_len = max(odd, even)

            if max_len > (end - start + 1):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]

class SolutionLC:
    # LC: https://leetcode.com/problems/longest-palindromic-substring/
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        end = 0

        def expandAroundCenter(left, right):
            # Expand as long as we are within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length (e.g., "aba")
            len1 = expandAroundCenter(i, i)
            # Case 2: Even length (e.g, "abba")
            len2 = expandAroundCenter(i, i + 1)

            max_len = max(len1, len2)

            if max_len > (end - start):
                # Update start/end based on the new center and length
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.longestPalindrome("forgeeksskeegfor")}")
print(f"LC Solution: {solutionGFG.longestPalindrome("Geeks")}")