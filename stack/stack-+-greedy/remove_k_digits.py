"""
Intuition
The goal is to make the number as small as possible. In any multi-digit number, the leftmost digits have the highest "weight" (place value). Therefore, a smaller digit at a higher place value is always better than a smaller digit at a lower place value. To achieve this, we want the digits to be in non-decreasing order (e.g., 1234). If we encounter a digit that is smaller than the one before it (a "peak" or "cliff"), removing the larger preceding digit will immediately result in a smaller number.

Example: num = 1432, k = 1
    - If we remove 1 -> 432
    - If we remove 4 -> 132 (Winner! Because 4 was a "peak" followed by a smaller 3).

Approach: Monotonic Stack
We use a stack to maintain a non-decreasing sequence of digits.
    1. Iterate through each digit in the string.
    2. While the stack is not empty, k > 0, and the current digit is smaller than the top of the stack:
        - Pop the stack (remove the "peak" digit).
        - Decrement k.
    3. Push the current digit onto the stack.
    4. Edge Case (Remaining K): If we finish the loop and k is still > 0 (meaning the number was already non-decreasing, like 1234), remove the remaining k digits from the end of the stack.
    5. Clean up: Convert the stack back to a string, remove any leading zeros and return "0" if the resulting string is empty.

Complexity Analysis
Time Complexity: O(N)
    - We traverse the input string of length N exactly once.
    - Each digit is pushed onto the stack once and popped at most once. Even though there is a nested while loop, the total number of operations is linear because each element enters and leaves the stack only one time.

Space Complexity: O(N)
    - In the worst case (where the digits are already in increasing order), we store all N digits in the stack.

Key Takeaways for the Interviewer
    - Greedy Choice: We make the locally optimal choice (removing a peak) to reach the globally optimal solution.
    - Monotonicity: Recoginizing that a "monotonic increasing" stack keeps the smallest digits at most significant positions.
    - Edge Case Handling: Explicitly handling leading zeros and cases where k is equal to the length of the string.
"""


class Solution:
    # LC: https://leetcode.com/problems/remove-k-digits/
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # While we have removals left and the current digit
            # is smaller than the last one added, pop the stack.
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0, remove from the end (for cases like "1234'")
        final_stack = stack[:-k] if k > 0 else stack

        # Convert to string and strip leading zeros
        result = "".join(final_stack).lstrip("0")

        return result if result else "0"

    # GFG: https://www.geeksforgeeks.org/problems/remove-k-digits/1
    def removeKdig(self, s, k):
        # code here
        stack = []

        for digit in s:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        final_stack = stack[:-k] if k > 0 else stack
        result = "".join(final_stack).lstrip("0")

        return result if result else "0"

solution = Solution()
print(f"LC Solution: {solution.removeKdigits("4325043", 3)}")
print(f"GFG Solution: {solution.removeKdig("4325043", 3)}")