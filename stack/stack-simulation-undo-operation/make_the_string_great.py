"""
Time Complexity: O(n)
We perform a single pass through the string of length n. Each character is either pushed onto the stack or popped off exactly once. Since stack operations (push and pop) are O(1), the total time is linear.

Space Complexity: O(n)
In the worst-case scenario (e.g., a string like "abcdef" where no two adjacent characters trigger the "bad" condition), the stack will eventually store every character from the input string.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/make-the-string-great/
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


"""
Intuition
The core of this problem is understanding "cyclic distance."
Imagine the alphabet on a circular clock: "a" is at 12 o'clock,
'b' is at 1 o'clock, and 'z' is at 11 o'clock.
    - The distance between two letters is the number of
    steps to get from one to the other.
    - In a circle of 26 letters, the maximum distance
    between any two points is 13.
    - If the absolute difference between two characters is d,
    the cyclic distance is min(d, 26-d).

Approach:
    1. Iterate through the string from the first character
to the second-to-last character.
    2. For each character s[i] and its neighbor s[i+1], 
    calculate the numerical difference using their ASCII values
    (ord() in Python).
    3. Calculate the absolute difference: diff = |ord(s[i])-ord(s[i+1])|.
    4. Validate the "Good" condition:
        - The distance is 1 if diff = 1 (e.g., "a" to "b" or "c" to "b").
        - The distance is also 1 if diff = 25 (e.g., "a" to "z" or "z" to "a").
    5. If any adjacent pair fails this check, immediately return "NO".
    6. If you finish the loop without issues, return "YES".

Time Complexity: O(N)
We perform a single pass through the string length N. Each
comparison and calculation inside the loop takes O(1) constant
time.

Space Complexity: O(1)
We are not using extra data structures (like HashMaps
or Lists) that scale with the input size. We only use
a few integer variables for the loop and calculations.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/good-string5712/1
    def isGoodString(self, s):
        # code here
        # Edge case: Unit lenght strings are always good.
        if len(s) <= 1:
            return "YES"

        for i in range(len(s) - 1):
            # Calculate absolute difference in ASCII values
            diff = abs(ord(s[i]) - ord(s[i + 1]))

            # Distance is 1 if they are adjacent (diff 1)
            # or wrap-around adjacent (diff 25)
            if diff != 1 and diff != 25:
                return "NO"

        return "YES"

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.makeGood("leeeEtcode")}")
print(f"GFG Solution: {solutionGFG.isGoodString("cbaz")}")