"""
1. Intuition
If we are looking for a permutation of s1 (length L1) inside s2, we are essentially looking for a fixed-size window of length L1 in s2 where the count of each character matches the count of characters in s1.

Instead of generating all permutations (which is O(n!) and impossible for the given constraints), we use a Sliding Window combined with a Frequency Map (or Hash Table). As we slide the window one character to the right, we don't need to re-count everything; we simply "add" the new character entering the window and "remove" the old character leaving it.

2. Approach: Sliding Window (Optimal)
    1. Edge Case: If len(s1) > len(s2), it's impossible for s2 to contain a permutation of s1. Return False.
    2. Initialize Maps: Create two frequency arrays (size 26 for lowercase English letters).
        - count_s1: Frequencies of characters in s1.
        - window_s2: Frequencies of characters in the first window of s2 (from index 0 to len(s1) - 1).
    3. Initial Comparison: If count_s1 == window_s2, we found a match immediately. Return True.
    4. Slide the Window: Iterate from index len(s1) to the end of s2:
        - Add the character at the current index to window_s2
        - Remove the character that is now outside the window (at index - len(s1)).
        - Compare the maps again. If they match, return True.
    5. Conclusion: If the loop finishes without a match, return False.

Time Complexity: O(L1 + (L2-L1) x 26)
    - Initialization: We spend O(L1) to populate the initial frequency maps.
    - Sliding: We iterate through s2 once (L2 - L1 steps).
    - Comparison: In each step, we compare two arrays of size 26. While technically O(1) because 26 is a constant, in a FAANG interview, you should acknowledge it as O(sigma) where sigma is the alphabet size.
    - Overall: This simplifies to O(L2) for most practical purposes.

Space Complexity: O(1)
    - We use two frequency arrays of size 26. Since the size of the alphabet (lowercase English) is fixed and dodes not grow with the input size n, the space complexity is constant.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/permutation-in-string/
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Build initial frequency maps
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1

        if s1_counts == s2_counts:
            return True

        # Slide the window across s2
        for i in range(n1, n2):
            # Add new character
            s2_counts[ord(s2[i]) - ord("a")] += 1
            # Remove character falling out of window
            s2_counts[ord(s2[i - n1]) - ord("a")] -= 1

            if s1_counts == s2_counts:
                return True

        return False

# User function Template for python3

"""
1. Sort the input string: This ensures that when we pick
characters for our permutations, we generate them in
alphabetical order.
2. Use a frequency map/used array: Keep track of which
characters from the original string have already been
added to the current permutation.
3. Recusive Backtracking:
    - Base Case: If the lenght of the current permutation
    equals the length of the input string, add it to our
    result list.
    - Recursive Step: Loop through the sorted characters. if
    a character hasn't been used, "choose" it, move to the
    next level of recursion, and then "un-choose" it (backtrack)
    to try the next possibility.

Time Complexity: O(NxN!)
The time complexity is dominated by the number of permutations
generated and the work done at each step.
    - Number of Permutations: For a string of length N, there are
    N! (N factorial) possible permutations when treating each
    character as unique.
    - Work per Permutation
        - Building the String: When the base case is reached,
        "".join(curr) takes O(N) time to create the string
        from the list.
        - Sorting: The final res.sort() takes O(K log K)
        where K = N!. However, O(NxN!) is tighter upper
        bound for the recursive generation process itself.

Space Complexity: O(NxN!)
The space complexity is determined by both the recursion
depth and the storage of the results.
    - Recursion Stack: The depth of the recursive calls is
    equal to the length of the string, which is O(N).
    - Auxiliary Space: We use a used array of size O(N) and
    a temporary list curr of size O(N).
    - Output Storage: The primary space consumer is the res
    list, which stores N! strings, each of length N. This
    results in a total space requirement of O(NxN!)
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/permutations-of-a-given-string-1587115620/1
    def permutation(self, s):
        res = []
        chars = sorted(list(s))
        used = [False] * len(chars)

        def backtrack(curr):
            if len(curr) == len(chars):
                res.append("".join(curr))
                return

            for i in range(len(chars)):
                # Character already used in this specific permutation path
                if not used[i]:
                    # Choose the character
                    used[i] = True
                    curr.append(chars[i])

                    # Explore
                    backtrack(curr)

                    # Backtrack
                    curr.pop()
                    used[i] = False

        backtrack([])
        res.sort()
        return res

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.checkInclusion("ab", "eidbaooo")}")
print(f"GFG Solution: {len(solutionGFG.permutation("ABSG"))}")