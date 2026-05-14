"""
Intuition
The goal is to find the lexicographically smallest subsequence that contains all unique characters of the input string.
    - The Conflict: If we see 'b' then 'a', we want 'a' to come first because "ab" < "ba".
    - The Constraint: We can only move 'a' before 'b' if there is another 'b' later in the string. If the current 'b' is the last one available, we must keep it where it is, even if a smaller letter follows it.
    - The Too: A Stack allows us to look at the "most recent" characters and decide if they should be replaced by a smaller incoming character.

Approach: Monotonic Stack + Greedy
We process the string character by character maintaining a stack that stays as "alphabetical" as possible.
    1. Preprocessing: Create a frequency map (or last_occurrence index map) so we know if a character appears again later.
    2. Iterate: For every character c in the string:
        - Skip: If c is already in our stack (tracked by a visited set), skip it to maintain uniqueness.
        - Pop (The Greedy Part): While the stack is not empty, the top of the stack stack[-1] is greater than s, and stack[-1] appears again later in the string:
            - Pop from the stack.
            - Remove from the visited set
        - Push: Add c to the stack and the visited set.
    3. Result: The stack now contains the smallest valid subsequence.

Complexity Analysis
Time Complexity: O(N)
We traverse the string once (N). Each character is pushed and popped from the stack at most once.

Space Complexity: O(1) or O(sigma)
Although we use a stack and a set, the size is capped by the number of unique characters in the alphabet (max 26 for lowercase English), which is constant.
"""


class Solution:
    # LC: https://leetcode.com/problems/remove-duplicate-letters/
    def removeDuplicateLetters(self, s: str) -> str:
        # Map to track the last index of every character
        last_occ = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue

            # While char is smaller than stack top and stack top appears later
            while stack and char < stack[-1] and i < last_occ[stack[-1]]:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return "".join(stack)

solution = Solution()
print(f"LC Solution: {solution.removeDuplicateLetters("bcabc")}")