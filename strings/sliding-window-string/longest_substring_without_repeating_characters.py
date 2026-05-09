"""
Questions:
Can s be empty?
What characters does s have? Are uppercase and lowercase considered the same?

TC: O(n) where n is the number of characters in s
SC: O(n) where n is the number of characters in s if all characters are unique
Refinement: More specifically, the space complexity is O(k) where k is the size of the character set (e.g., 26 for lowercase English,
or 128/256 for ASCII). The set has_seen will never grow larger than the number of unique characters available in the character set
or the length of the string itself.
"""


class Solution:
    # LC: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s: str) -> int:
        has_seen = set()
        left = 0
        n = len(s)
        longest = 0

        for right in range(n):
            while s[right] in has_seen:
                has_seen.remove(s[left])
                left += 1

            longest = max(longest, right - left + 1)
            has_seen.add(s[right])

        return longest

    def longestUniqueSubstr(self, s):
        # GFG: https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1
        # code here
        has_seen = set()
        left = 0
        longest = 0
        n = len(s)

        for right in range(n):
            while s[right] in has_seen:
                has_seen.remove(s[left])
                left += 1
            longest = max(longest, right - left + 1)
            has_seen.add(s[right])

        return longest

solution = Solution()
print(f"GFG Solution: {solution.longestUniqueSubstr("geeksforgeeks")}")
print(f"LC Solution: {solution.lengthOfLongestSubstring("abcabcbb")}")