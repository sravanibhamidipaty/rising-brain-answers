"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/container-with-most-water0535/1
    def maxWater(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        maximum_area = float("-inf")

        while left < right:
            current_area = (right - left) * min(arr[left], arr[right])
            maximum_area = max(current_area, maximum_area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return maximum_area if maximum_area != float("-inf") else 0


"""
Questions: 
Can height be negative?
Can height be empty?
Is height integers?

Intuition:
Two pointers pattern

Approach:
Two pointers left and right left is at index 0 and right is at index len(height)-1 last number in the array.
If height[left] < height[right] increase left pointer maybe the next height is greater than the current height, so
we can check that height. Otherwise, move the right pointer, if the heights are equal, it doesn't matter which one we move

TC: O(n) where n is the number of elements in the height array
SC: O(1) we are only using 3 variables
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/container-with-most-water/
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum_area = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            maximum_area = max(current_area, maximum_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum_area

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.maxWater([1, 5, 4, 3])}")
print(f"LC Solution: {solutionLC.maxArea([1,8,6,2,5,4,8,3,7])}")