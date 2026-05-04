"""
Intuition: Nested for loops O(n^2) TC and O(1) SC

Approach: Hash map + for loop

TC: O(n) where n is the number of elements in arr
SC: O(n) where n is the number of elements in arr
"""

from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1
    def countPairs(self, arr, target):
        # Complete the function
        number_counter = {}
        result = 0

        for num in arr:
            diff = target - num
            if diff in number_counter:
                result += number_counter[diff]
            number_counter[num] = number_counter.get(num, 0) + 1
        return result


class SolutionLC:
    # LC: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.countPairs([-1, 1, 5, 5, 7], 6)}")
print(f"Leetcode Solution: {solutionLC.twoSum([2,7,11,15], 9)}")