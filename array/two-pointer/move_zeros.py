"""
Questions:
- Can nums be empty?
- Can nums only have zeros as input?
- Can nums not have zeros as a part of the input?

Intuition: Create another array with 0s. TC: O(n) SC: O(n) where n is the number of elements in the list

Approach: Two pointers

Time Complexity: O(n) where n is the number of elements in the list because I am looping through using
a for loop

Space Complexity: O(1) where I am only using pointers

nums = [0, 1, 0, 3, 12]
fast = 0: [0, 1, 0, 3, 12], slow = 0
fast = 1: [1, 0, 0, 3, 12], slow = 1
fast = 2: [1, 0, 0, 3, 12], slow = 2
fast = 3: [1, 2, 0, 0, 12], slow = 3
fast = 4: [1, 2, 12, 0, 0], slow = 4
"""

from typing import List

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
    def pushZerosToEnd(self, arr):
        # code here
        left = 0
        n = len(arr)

        for right in range(n):
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        return arr

    # LC: https://leetcode.com/problems/move-zeroes/
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

solution = Solution()
print(solution.pushZerosToEnd([1, 2, 0, 3]))
print(solution.moveZeroes([1, 2, 0, 3]))