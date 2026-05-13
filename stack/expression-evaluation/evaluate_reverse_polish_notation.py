from typing import List
from math import floor

"""
Evaluates an arithmetic expression in Reverse Polish Notation.

Intuition:
In RPN, operators follow their operands. A Stack is the natural data
structure here because we need to process the most recently seen
numbers first when an operator appears (LIFO).

Approach:
1. Initialize an empty stack.
2. Iterate through each token:
   - If it's an operand (number), push it to the stack.
   - If it's an operator (+, -, *, /), pop the top two numbers.
   - IMPORTANT: The first pop is the divisor/subtrahend (b),
     the second pop is the dividend/minuend (a).
3. Perform the calculation and push the result back.
4. Return the last remaining element in the stack.

Note on Division:
Python's // operator floors towards negative infinity. The problem
requires truncation toward zero, achieved by int(a / b).

Args:
    tokens (list[str]): A list of strings representing the expression.

Returns:
    int: The final value of the arithmetic expression.

Complexity Analysis:
    Time Complexity: O(n)
        - We iterate through the 'n' tokens exactly once.
        - Each stack push/pop operation is O(1).
    Space Complexity: O(n)
        - In the worst case (all operands followed by all operators),
          the stack grows to size 'n'.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/evaluate-reverse-polish-notation/
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(b + a)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(b * a)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return sum(stack)



class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1
    def evaluatePostfix(self, arr):
        # code here
        stack = []

        for char in arr:
            if char == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif char == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(floor(a / b))
            elif char == "^":
                b = stack.pop()
                a = stack.pop()
                stack.append(a**b)
            else:
                stack.append(int(char))

        return stack[0]

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.evalRPN(["4","13","5","/","+"])}")
print(f"GFG Solution: {solutionGFG.evaluatePostfix(["2", "3", "^", "1", "+"])}")