"""
Intuition
The core challenge is the nested nature of the encoding (e.g., 3[a2[c]]). When you see nested structures where the innermost part needs to be resolved first, your mind should immediately jump to a Stack or Recursion.

Think of it like solving a math equation with parentheses: 3 x (a + 2 x (c)). You can't resolve the outer multiplication until you know what's inside the innermost bracket.

Approach: The Two-Stack Strategy
Iterate through the string:
    1. If Digit: Build the full number (it could be multiple digits like 100).
    2. If [ (Opening Bracket): We've finished building the number and are starting a new nested layer. Push the current number onto the countStack and the current string onto the stringStack. Reset them for the new scope.
    3. If Letter: Just append it to the current string.
    4. If ] (Closing Bracket): A nested layer is finished.
        - Pop the repeat count (k) from countStack.
        - Pop the previously stored string from stringStack.
        - Repeat the current string k times and append it to the popped string.

Time Complexity: O(N)
    - We iterate through the input string s of length N once.
    - While string concatenation and repetition take time proportional to the output length, the problem guarantees the output will not exceed 10**5.
    - In Big O terms relative to the input, we process every character once, so it is Linear.

Space Complexity: O(N)
    - Stack Space: In the worst case of deeply nested strings (e.g., 1[1[1[1[a]]]]), the stacks will grow proportional to the number of brackets in the input string.
    - Resultant String: We also store the decoded string, which contributes to the space used during the process.
"""
class SolutionTwoStack:
    # LC: https://leetcode.com/problems/decode-string/
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        current_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                # Handle multi-digit number (e.g., "100[a]")
                k = k * 10 + int(char)
            elif char == "[":
                # Entering a new level: save current state
                countStack.append(k)
                stringStack.append(current_string)
                # Reset for the content inside brackets
                current_string = ""
                k = 0
            elif char == "]":
                # Leaving a level decode and merge
                repeat_times = countStack.pop()
                last_string = stringStack.pop()
                current_string = last_string + (current_string * repeat_times)
            else:
                # It's a character
                current_string += char
        return current_string

"""
Intuition: The Single-Pipe Processing
In the two-stack approach, we pre-emptively separated counts and strings. With one stack, you push everything onto the stack, including digits and the opening bracket [, and only perform the decoding when you hit a closing bracket. This mimics how a compiler might parse nested expressions. When you hit ], you look back through the stack until you find the corresponding [, process that segment, and push the result back onto the stack to be potentially used by a further outer layer.

Approach: Single Stack Walkthrough
    1. Iterate through the string:
        - If it's not ]: Push the character onto the stack. (Note: For digits, you still need to pre-calculate the full number if it has multiple digits, then push that number as a single element).
        - If it's ]:
            1. Pop characters until you hit [ to get the "encoding string" inside the brackets.
            2. Pop the [ (discard it).
            3. Pop the next element, which will be the multiplier k.
            4. Repeat the string k times and push it back onto the stack as a combined string.
    2. Final Step: Join all remaining elements in the stack into a single string.

Time Complexity: O(max(K)*N)
While it is technically linear relative to the size of the output, in an interview, you should mention that string concatenation inside the loop (segment = stack.pop() + segment) can be O(M) where M is the length of the segment. However, because the problem constraints limit the total output lenght to 10**5, remains efficient.

Space Complexity: O(Output Length)
In the worst case, the stack stores the entire decoded string characters before the final join().
"""


class SolutionOneStack:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                # Push the multiplier and reset
                stack.append(curr_num)
                stack.append("[")
                curr_num = 0
            elif char == "]":
                # Step 1: Pop the string to be repeated
                segment = ""
                while stack and stack[-1] != "[":
                    segment = stack.pop() + segment

                # Step 2: Pop the '['
                stack.pop()

                # Step 3: Pop the multiplier k
                k = stack.pop()

                # Step 4: Repeat and push back
                stack.append(segment * k)
            else:
                # It's a regular letter
                stack.append(char)
        return "".join(stack)

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/decode-the-string2444/1
    def decodedString(self, s):
        # code here

        stack = []
        current_num = 0

        for char in s:  # 3[ab]
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # 3
            elif char == "[":
                stack.append(current_num)  # 3
                stack.append("[")  # [ stack = 3[ab
                current_num = 0
            elif char == "]":
                segment = ""
                while stack[-1] != "[":
                    segment = stack.pop() + segment  # ab
                stack.pop()
                k = stack.pop()  # 3
                string = segment * k
                stack.append(string)  # ababab
            else:
                stack.append(char)

        return "".join(stack)

solutionTwoStack = SolutionTwoStack()
solutionOneStack = SolutionOneStack()
solutionGFG = SolutionGFG()
print(f"LC Solution Two Stack: {solutionTwoStack.decodeString("3[a]2[bc]")}")
print(f"LC Solution One Stack: {solutionOneStack.decodeString("3[a]2[bc]")}")
print(f"GFG Solution One Stack: {solutionGFG.decodedString("3[a]2[bc]")}")