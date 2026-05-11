from typing import List

"""
Intuition
The core of this problem is managing order-dependent interactions. When a new asteroid enters from the right, it only cares about the asteroid immediately to its left.
    - If they move apart (Left <--> Right), they never meet.
    - If they move together (Right-><-Left), they collide.
Since a single left-moving asteroid can cause a "chain reaction" of collisions (destroying multiple right-moving ones before finally settling or exploding itself), we need a way to look back at the most recent survivors. This "Last-In, First-Out" behavior is the classic signal to use a Stack.

The Approach: Linear Simulation with a Stack
We iterate through the asteroids one by one. For each asteroid, we treat it as a new "attacker" coming from the right.
    1. No Collision Case: If the asteroid is moving Right (> 0), or if the stack is empty, or if the top of the stack is moving Left (< 0), there is no collision. We simply push it onto the stack.
    2. Collision Case: If the stack is + and the current asteroid is -, a collision occurs:
    - Attacker is larger: pop() the stack and keep checking the new top (the attacker "survives" the current hit).
    - It's a tie: Both are destroyed. pop() the stack and stop processing the attacker.
    - Attacker is smaller: The attacker is destroyed. Stop processing and move to the next asteroid in the input.

Time Complexity: O(n)
Even though there is a while loop inside a for loop, notice that each asteroid is pushed onto and popped from the stack at most once. In the worst-case scenario (e.g., [1, 2, 3, 4, -5]), we do several pops in one go, but we can't pop more elements than we have previously pushed. This is called amortized analysis, resulting in a linear time complexity where n is the number of asteroids.

Space Complexity: O(n)
In the worst case (e.g., all asteroids moving in the same direction like [1, 2, 3, 4]), no collisions occur and the stack will store all n asteroids. The space used is proportional to the number of asteriods that survive.

Edge Cases
    1. Empty Result: [8, -8] -> []
    2. No Collisions: [-2, -1, 1, 2] -> They are moving away from each other.
    3. Massive Chain Reaction: [10, 2, -5] -> -5 destroys 2, then 10 destroys -5. Final: [10].
"""


class Solution:
    # LC: https://leetcode.com/problems/asteroid-collision/description/
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Collision condition: stack top moving Right (+) and current moving Left (-)
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue  # Attacker wins, check the next one on stack
                elif stack[-1] == -asteroid:
                    stack.pop()  # Tie, both destroyed
                break  # Attacker was destroyed or it was a tie.
            else:
                # Only runs if the attacker survived all collisions (no break hit)
                stack.append(asteroid)

        return stack

solutionLC = Solution()
print(f"LC Solution: {solutionLC.asteroidCollision([5,10,-5])}")