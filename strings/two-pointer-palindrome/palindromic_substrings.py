"""
Questions:
    Case Sensitivity: Does the string consist only of lowercase English letters, or should 'Aa' be considered a palindrome?
    Empty strings: What should we return for an empty string? Based on the constraints (1 <= s.length), s will have at least one character.
    Definition of Substring: Just to confirm, we are looking for contiguous sequences, not subsequences, correct?

Intuition:
The "Brute Force" Thought: I could check every possible substring (there are O(n^2) of them) and verify if each is a palindrome (O(n) check). This would result in an O(n^3) time complexity, which is inefficient for a string of length 1,000.

The Expand Around Center Intuition:
Instead of picking a substring and checking if it's a palindrome, we can pick a center and expand outwards as long as the characters match.
    - A palindrome can have odd length (centered on one character, like "aba") or an even length (centered between two characters like "abba").
    - For a string of length n, there are 2n - 1 possible centers (each character and each gap between characters).

Time Complexity: O(n^2). We iterate through 2n - 1 centers, and for each center, we expand up to n times. n (characters) + (n-1) (gaps) = 2n-1 total centers.
Space Complexity: O(1). We are only using a few variables to track the count and pointers; we don't need extra data structures like a DP table.

Let's dry run with Example 2: s = "aaa"

i = 0:
Expand(0, 0): s[0]==s[0] ('a'). Count = 1. Pointers move to (-1, 1) -> Stop.
Expand(0, 1): s[0]==s[1] ('a'=='a'). Count = 2. Pointers move to (-1, 2) -> Stop.

i = 1:
Expand(1, 1): s[1]==s[1] ('a'). Count = 3. Pointers move to (0, 2). s[0]==s[2] ('a'=='a'). Count = 4. Pointers move to (-1, 3) -> Stop.
Expand(1, 2): s[1]==s[2] ('a'=='a'). Count = 5. Pointers move to (0, 3) -> Stop.

i = 2:
Expand(2, 2): s[2]==s[2] ('a'). Count = 6. Pointers move to (1, 3) -> Stop.
Expand(2, 3): Right is out of bounds -> Stop.

Final Result: 6. This matches the Example 2 output.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1
    def countPS(self, s):
        # code here
        self.count = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 2:
                    self.count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return self.count


class SolutionLC:
    # LC: https://leetcode.com/problems/palindromic-substrings/
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        n = len(s)
        for i in range(n):
            self.expand(s, i, i)
            self.expand(s, i, i + 1)
        return self.count

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.count += 1
            left -= 1
            right += 1

solutionGFG = SolutionGFG()
print(f"GFG Solution: {solutionGFG.countPS("abaab")}")
solutionLC = SolutionLC()
print(f"LC Solution: {solutionLC.countSubstrings("abc")}")