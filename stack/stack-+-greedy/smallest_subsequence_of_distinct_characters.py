"""
Time Complexity: O(N)
    - Last Occurrence Map: Creating the last_occ dictinoary takes O(N) as you iterate through the string once.
    - Main Loop: You iterate through each character in the string s once.
    - Stack Operations: While there is a while loop inside the for loop, each character is pushed onto the stack at most once and popped from the stack at most once. This results in an amortized time complexity of O(N).

Space Complexity: O(sigma)
    - Character Set: The space used by last_occ, visited, and the stack is proportional to the number of unique characters in the input string.
    - In this specific LeetCode problem, the input is restricted to lowercase English letters, so sigma = 26, making it effectively O(1) in practice. However, if the character set were larger (like Unicode), it would scale with the number of unique elements (O(sigma)).
"""


class Solution:
    # LC: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {char: i for i, char in enumerate(s)}
        visited = set()
        stack = []

        for i, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return "".join(stack)

solution = Solution()
print(f"LC Solution: {solution.smallestSubsequence("bcabc")}")