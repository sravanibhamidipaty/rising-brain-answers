"""
Intuition
The problem asks us to remove adjacent duplicates repeatedly. When you remove a pair (like "bb" in "abbaca"), the characters that were previously separated (the two "a"s) now become adjacent. This "last-in, first-out" behavior--where the most recently kept character needs to be compared with the next incoming character--is a classing indicator for a Stack data structure.

2. Approach
We iterate through the string and maintain a stack of characters that we have decided to "keep" so far.
    - Step 1: Initialize an empty list (stack).
    - Step 2: For each character in the input string:
        - Check if the stack is empty and the top of the stack is equal to the current character.
        - If they match, we found an adjacent duplicate! Pop the character from the stack and discard the current character.
        - If they don't match (or the stack is empty), push the current character onto the stack.
    - Step 3: Convert the stack (which now contains only the remaining characters) back into a string and return it.

Time Complexity: O(n)
    - We traverse the string exactly once, where n is the length of the string.
    - Each character is pushed and popped from the stack at most once.
    - In Python, "".join(stack) also takes O(n) time.
    - Total: O(n).

Space Complexity: O(n)
    - In the worst-case scenario (e.g., "abcdef"), there are no duplicates, and the stack will store all n characters.
    - Even though we are returning a string, the stack itself requires extra linear space during processing.
    - Total: O(n).
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            # If the current char matches the last one we addded,
            # they are adjacent duplicates; remove the match.
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # Otherwise, keep the current character for now.
                stack.append(char)

        # Join the remaining characters in the stack to
        # form the result string.
        return "".join(stack)

"""
Problem: Given a string s and an integer k, the task is to repeatedly delete k adjacent duplicates till no deletions are possible and then return the final string. On deletion of k adjacent duplicates, the left and right sides of the deleted substring is concatenated together.

Approach: Stack of Pairs
Instead of just storing characters, we store a pair (or a small object)
in our stack: (character, consecutive_count).
1. Iterate through each character c in the input string.
2. Check the Stack:
    - If the stack is not empty and the top character is equal to c:
        - Increment the count of the top element: stack[-1][1] += 1
        - Check for k: If the new count equals k, pop the element off the stack
    - If the stack is empty or the top character is not c:
        - Push a new pair onto the stack: (c, 1)
3. Reconstruct: After the loop, the stack contains only the characters that didn't form a group of k. Iterate through the stack to build the final string based on the remaining counts.

Time Complexity: O(n)
    - We traverse the input string exactly once.
    - Each character is pushed and popped from the stack at most once.
    - Building the final string takes O(n) time in the worst case (if no characters are deleted).
    - Thus, the total time complexity is linear relative to the length of the string n.

Space Complexity: O(n)
    - In the worst case (where no k adjacent duplicates exist), the stack will store all n characters.
    - Even though we store pairs, the space remains proportional to n.
"""

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/dsa/remove-all-adjacent-duplicates-in-string-ii/
    def removeDuplicates(self, s: str, k: int) -> str:
        # Each element in stack will be [character, character_count]
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                # Increment the count of the existing top character
                stack[-1][1] += 1

                # If count reaches k, "explode" the group by popping
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # New character or different from top, start a new count
                stack.append([char, 1])

        # Reconstruct the string from the remaining characters and their counts
        return "".join(char*count for char, count in stack)

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.removeDuplicates("abbaca")}")
print(f"GFG Solution: {solutionGFG.removeDuplicates("deeedbbcccbdaa", 3)}")