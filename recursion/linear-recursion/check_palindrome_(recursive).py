"""
Intuition
A palindrome reads the same forward and backward. The core
recursive intuition is that a number is a palindrome if:
    1. The first and last digits match.
    2. The remaining inner part of the number is also a
    palindrome.
Since the problem statement explicitly mentions ignoring
the sign (e.g., -121 is true), our first step is to treat
the number to a string makes accessing the ends much simpler
for a recursive approach.

Approach
1. Preprocessing: Convert the integer n to its absolute
value and then to a string.
2. Base Cases:
    - If the string has 0 or 1 character, it is a palindrome.
    Return True
3. Recursive Step:
    - Compare the first character (s[0]) with the last character
    (s[-1]).
    - If they don't match, return False.
    - If they match, call the function recursively on the
    substring excluding the first and last characters (s[1:-1]).

Complexity Analysis
Time Complexity: O(d)
    - Where d is the number of digits in the integer n. Each
    recursive call processes two digits (the start and the
    end). In the worst case, we peform d/2 comparisons.

Space Complexity: O(d)
    - String Storage: O(d) to store the string representation.
    - Recursion Stack: O(d) due to the depth of the recursive
    calls. In a production environment, an iterative
    approach would be preferred to achieve O(1) space,
    but for a "recursive" requirement, this is the standard
    cost.
"""


class SolutionRecursive:
    # GFG: https://www.geeksforgeeks.org/problems/palindrome0746/1
    def isPalindrome(self, n):
        # code here
        # FAANG Tip: Clarify the sign constraint.
        # The problem states to ignore signs.
        s = str(abs(n))

        def check(sub_s):
            # Base case: empty or single char string
            if len(sub_s) <= 1:
                return True

            # Check outer boundaries
            if sub_s[0] != sub_s[-1]:
                return False

            # Recursive call on the middle part
            return check(sub_s[1:-1])

        return check(s)

solutionRecursive = SolutionRecursive()
print(f"GFG Solution Recursive: {solutionRecursive.isPalindrome(555)}")