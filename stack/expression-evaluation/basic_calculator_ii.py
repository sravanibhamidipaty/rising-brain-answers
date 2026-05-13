"""
Questions:
    - Non-negative integers: The problem states integers are non-negative, but should I handle negative results during intermediate steps? (e.g., 3-5+2)
    - Spaces: Does the string contain spaces, and should they be ignored?
    - Division: Should I use floor division? How should it handle negative results (truncate toward zero or floor)?
    - Bounds: Will the expression always be valid, or should I handle syntax errors?

Intuition:
We must respect the Order of Operations. Multiplication and division have higher precedence than addition and subtraction.
    - Initial Thought: We could use a stack to store numbers.
    - Handling Precedence: If we see + or -, we can't solve it immediately because the next term might be multiplied.
        - If we see * or / we can solve it immediately with the last number we saw.

Approach:
    1. Keep track of the current_number being parsed.
    2. Keep track of the last_operator seen (initialize as +).
    3. When we hit a new operator or  the end of the string:
        - If last_operator was +: Push current_number to stack.
        - If last_operator was -: Push - current_number to stack.
        - If last_operator was *: Pop the top of the stack, multiply it by current_number, and push the result back.
        - If last_operator was /: Pop the top, divide by current_number (truncate toward zero), and push back.


Time Complexity: O(n) where n is the length of the string. We iterate through the string exactly once.
Space Complexity: O(1) due to the result variable.


Comparison of the two scenarios:

Scenario A: 3 + 5 + 2
Reach first +: result stays 0, last_num becomes 3.
Reach second +: Now we know 3 is safe. result becomes 3. last_num becomes 5.
Reach end: result (3) + last_num (5 + 2) = 10.

Scenario B: 3 + 5 * 2
Reach +: result stays 0, last_num becomes 3.
Reach *: Now we know 3 is safe because * only affects the number immediately before it (5). result becomes 3. last_num becomes 5.
Reach end: Since the last_op was *, we do last_num = 5 * 2 = 10.
Final: result (3) + last_num (10) = 13.

Meta Interview Tip: Truncation
In the dry run, always mention the division truncation. In Python, 5 // 2 is 2, but -5 // 2 is -3. The problem requires truncation toward zero, so -5 / 2 should be -2. Using int(last_num / current_num) is the safest way to ensure this behavior across all positive and negative cases.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/basic-calculator-ii/
    def calculate(self, s: str) -> int:
        last_number = 0
        current_number = 0
        last_operator = "+"
        res = 0

        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if not char.isdigit() and not char.isspace() or i == len(s) - 1:
                if last_operator == "+":
                    res += last_number
                    last_number = current_number
                elif last_operator == "-":
                    res += last_number
                    last_number = -current_number
                elif last_operator == "*":
                    last_number = last_number * current_number
                elif last_operator == "/":
                    last_number = int(last_number / current_number)
                last_operator = char
                current_number = 0

        res += last_number
        return res

