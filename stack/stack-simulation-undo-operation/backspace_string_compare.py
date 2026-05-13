"""
Intuition
The core challenge is the backspace character #. Because a # removes the most recently typed character, this follows a Last-In, First-Out (LIFO) pattern. Whenever we see a regular character, we want to "add" it to our current strring. Whenever we see a #, we want to "undo" the last addition. A stack is most natural data strcuture for this "undo" behavior.

Approach
1. Define a Helper Function: Create a function (e.g., buildStack) that processes a string and returns the "cleansed" result.
2. Iterate through the string:
    - If the character is not #, push it into the stack.
    - If the character is #, pop from the stack (if the stack is not empty).
3. Process both strings: Apply this logic to both s and t.
4. Compare: Convert the result stacks back into strings (or compare them directly) and return true if they match, otherwise false.

Time Complexity: O(N + M)
    - We iterate through string s exactly once (N) and string t exactly once (M).
    - Every stack operation (push and pop) takes O(1) constant time.
    - The final comparison of the two stacks also takes O(N + M) time.

Space Complexity: O(N + M)
    - In the worst-case scenario (where there are no backspaces), we store every character of both string in our stacks.
    - This results in linear space proportional to the input sizes.
"""


class SolutionLCStack:
    # LC: https://leetcode.com/problems/backspace-string-compare/
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str) -> list:
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return build(s) == build(t)


"""
Intuition (Backward Traversal)
If we start at the end of the string:
    - Every # we see increases a skip counter.
    - Every non-# character we can see either be "deleted" (if skip > 0) or it is part of our final comparison (if skip == 0).
    - BY doing this for both strings simultaneously, we can compare them character-by-character without ever storing a "cleansed" version.

Approach
1. Initialize two pointer i and j, at the end of s and t.
2. While either pointer is >= 0:
    - Find the next valid character for s:
        - If s[i] == "#": increment skipS, move i left.
        - Else if skipS > 0: decrement skipS, move i left.
        - Else: This is the character to compare.
    - Find the next valid character for t:
        - Apply the same logic using skipT and pointer j.
    - Compare:
        - If one string has a character and the other doesn't, or if the character differ, return false.
3. If we finish the loop without a mismatch, return True.

Complexity Analysis
Time Complexity: O(N + M)
We still visit every character in both strings at most once. The total operations scale linearly with the length of the input.

Space Complexity: O(1)
Unlike the stack approach, we only store a few integer variables (i, j, skip_s, skip_t). We do not create any new string or data structures that grow with the input size.
"""


class SolutionLCTwoPointers:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            # Find next valid char in s
            skip_s = 0
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # Find next valid char in t
            skip_t = 0
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Compare current characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            # If one string is exhausted but the other still has a valid char
            elif (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True


# User function Template for python3
"""
Intuition
The core challenge is that our "alphabet" isn't just single
characters; it includes a multi-character token ("ng").
Standard string comparison works by comparing characters
at the same index. However since "ng" is a single unit in
this language, a simple s1[i] == s2[i] check fails because
"n" followed by "g" has a different priority than "n" followed
by "o". We need a Two-Pointer Approach that can "look ahead"
to see if the next two characters form the special "ng" token.

Approach
We will use two pointers, i and j, to traverse s1 and s2
respectively.
    - Token Extraction: At each step, we determine the "current
    token" for both strings.
        - If s[i] is 'n' and s[i+1] is 'g', the token is "ng"
        and we move the pointer by 2.
        - Otherwise, the token is just s[i] and we move the
        pointer by 1.
    - Custom Comparison: If the tokens are identical, we
    continue to the next tokens.
        - If they differ, we compare them based on the rules:
        a < b < ... < n < ng < o.
    - Boundary Handling: If one string ends before the other,
    the shorter string is "lesser."

Time Complexity: O(N+M)
    - Where N and M are the lengths of s1 and s2. We traverse
    eaxh string at most once. Each "look-ahead" check is O(1).

Space Complexity: O(1)
    - We are not creating new substrings or utilizing extra
    data structures like hash maps. We only use a few interger
    variables for pointers and string flags.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/string-comparison5858/1
    def stringComparison(self, s1, s2):
        i, j = 0, 0
        n, m = len(s1), len(s2)

        # You MUST have this while loop to prevent Time Limit Exceeded
        while i < n and j < m:
            char1 = s1[i]
            len1 = 1
            if char1 == "n" and i + 1 < n and s1[i + 1] == "g":
                char1 = "ng"
                len1 = 2

            char2 = s2[j]
            len2 = 1
            if char2 == "n" and j + 1 < m and s2[j + 1] == "g":
                char2 = "ng"
                len2 = 2

            if char1 != char2:
                # Custom priority: n < ng < o
                if char1 == "ng":
                    return 1 if char2 <= "n" else -1
                if char2 == "ng":
                    return -1 if char1 <= "n" else 1

                return 1 if char1 > char2 else -1

            # Move the pointers
            i += len1
            j += len2

        # Handle length differences after the loop
        if i < n:
            return 1
        if j < m:
            return -1
        return 0

solutionLCTwoPointers = SolutionLCTwoPointers()
solutionLCStack = SolutionLCStack()
solutionGFG = SolutionGFG()
print(f"LC Solution Stack: {solutionLCStack.backspaceCompare("ab#c", "ad#c")}")
print(f"LC Solution Two Pointers: {solutionLCStack.backspaceCompare("ab#c", "ad#c")}")
print(f"GFG Solution: {solutionGFG.stringComparison("adding", "addio")}")