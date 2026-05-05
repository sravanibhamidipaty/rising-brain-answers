"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
    def sort012(self, arr):
        # code here
        left = 0
        right = len(arr) - 1

        current_index = 0

        while current_index <= right:
            if arr[current_index] == 0:
                arr[left], arr[current_index] = arr[current_index], arr[left]
                left += 1
                current_index += 1
            elif arr[current_index] == 2:
                arr[right], arr[current_index] = arr[current_index], arr[right]
                right -= 1
            else:
                current_index += 1

        return arr


class SolutionLC:
    # LC: https://leetcode.com/problems/sort-colors/description/
    def sortColors(self, arr: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(arr) - 1

        current_index = 0

        while current_index <= right:
            if arr[current_index] == 0:
                arr[left], arr[current_index] = arr[current_index], arr[left]
                current_index += 1
                left += 1
            elif arr[current_index] == 2:
                arr[right], arr[current_index] = arr[current_index], arr[right]
                right -= 1
            else:
                current_index += 1

        return arr


solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.sort012([0, 1, 2, 0, 1, 2])}")
print(f"LC Solution: {solutionLC.sortColors([2,0,2,1,1,0])}")