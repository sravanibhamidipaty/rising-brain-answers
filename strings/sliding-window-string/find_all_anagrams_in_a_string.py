from typing import List

"""
1. Intuition
The core of the problems is identifying anagrams. An anagram of a string p is simply any permutation of p. Instead of generating all n! permutations, we recognize a key property: two strings are angrams if and only if they have the same character frequencies.

Since we are looking for these frequencies within a continuous substring of s, we can imagine a window of length len(p) sliding across s. As the window moves, we don't need to re-calculate the entire frequency map; we only update the characters entering and leaving the window.

2. Approach: Sliding Window with Frequency Array
Since the input consists only of lowercase English letters, we can use a fixed-size array of length 26 instead of a hash map to save overhead.
1. Initialize: Create a frequency array p_count for string p and an empty frequency array s_count for the current window in s.
2. Initial Window: Fill s_count with the first len(p) characters of s.
3. Compare & Slide: *Compare s_count to p_count. If they match, the start index is an anagram.
    - Slide the window one character to the right:
        - Increment the count of the new character enter from the right.
        - Decrement the count of the character exiting from the left.
4. Edge Case: If len(p) > len(s), return an empty list immediately.

Time Complexity: O(N)
    - Initialization: We iterate over p once to build the initial count, which is O(M), where M is the length of p.
    - Sliding: We iterate over s once (N iterations). In each iteration, we perform O(1) updates to the frequency array.
    - Comparison: Comparing two arrays of size 26 is O(26), which is effectively O(1) constant time.
    - Total O(N), where N is the length of string s.

Space Complexity O(1)
    - We use two frequency arrays of size 26. Since the size of the alphabet is fixed and does not grow with the input size N or M, the space complexity is considered constant.
    - Note: The output list res is generally not counted toward space complexity in interview settings, but if it were, it would be O(N) in the worst case.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        if p_len > s_len:
            return []

        p_count = [0] * 26
        s_count = [0] * 26
        res = []

        # Build initial frequency maps
        for i in range(p_len):
            p_count[ord(p[i]) - ord("a")] += 1
            s_count[ord(s[i]) - ord("a")] += 1

        # Check the first window
        if s_count == p_count:
            res.append(0)

        # Slide the window across s
        for i in range(p_len, s_len):
            # Add new character remove old character
            s_count[ord(s[i]) - ord("a")] += 1
            s_count[ord(s[i - p_len]) - ord("a")] -= 1

            # Compare current window map with p's map
            if s_count == p_count:
                res.append(i - p_len + 1)

        return res


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
    def search(self, pat, txt):
        s_len, p_len = len(txt), len(pat)
        count = 0
        if p_len > s_len:
            return 0

        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(p_len):
            p_count[ord(pat[i]) - ord("a")] += 1
            s_count[ord(txt[i]) - ord("a")] += 1

        if s_count == p_count:
            count += 1

        for i in range(p_len, s_len):
            s_count[ord(txt[i]) - ord("a")] += 1
            s_count[ord(txt[i - p_len]) - ord("a")] -= 1

            if s_count == p_count:
                count += 1

        # This must be outside the for loop!
        return count

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"GFG Solution: {solutionGFG.search("for", "forxxorfxdofr")}")
print(f"LC Solution: {solutionLC.findAnagrams("cbaebabacd", "abc")}")