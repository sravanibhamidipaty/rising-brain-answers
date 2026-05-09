"""
Time Complexity: O(n)
    - The Logic: Although there is a while loop inside a for
    loop, the left pointer and the right pointer each travel
    across the string s at most once.
    - The Math: Each character is added to the dictionary
    once and removed at most once. This results in 2n
    total operations, which simplifies to O(n), where n
    is the length of the string.
    - Dictionary Operations: In Python, dictionary insertions,
    deletions, and lookups are O(1) on average.

Space Complexity: O(k) or O(1)
    - The Logic: You are storing character frequencies in the
    counts dictionary. The number of keys in this dictionary
    will never exceed k + 1.
    - The Constraint: The problem specifies the string consists
    of lowercase English alphabets. Therefore, the number
    of unique characters sigma is at most 26.
"""


class Solution:
    def longestKSubstr(self, s, k):
        # GFG: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
        # code here
        longest = -1
        left = 0
        n = len(s)

        # Use a dictionary to track character counts
        counts = {}

        for right in range(n):
            char_right = s[right]
            counts[char_right] = counts.get(char_right, 0) + 1

            # If we have more than k unique characters,
            # shrink from the left
            while len(counts) > k:
                char_left = s[left]
                counts[char_left] -= 1
                if counts[char_left] == 0:
                    del counts[char_left]
                left += 1

            # Check if we have exactly k unique characters
            if len(counts) == k:
                longest = max(longest, right - left + 1)

        return longest
