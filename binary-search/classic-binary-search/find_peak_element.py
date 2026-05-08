from typing import List

"""
Can nums be empty?
Is it guaranteed a peak exists?

Time Complexity: O(log n) due to binary search where n is the length of the nums List
Space Complexity: O(1) we are not storing it anywhere
"""


class Solution:
    # LC: https://leetcode.com/problems/find-peak-element/description/
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

    # GFG: https://www.geeksforgeeks.org/problems/peak-element/1
    def peakElement(self, arr):
        # Code here
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


solution = Solution()
print(f"GFG Solution: {solution.peakElement([1, 2, 4, 5, 7, 8, 3])}")
print(f"LC Solution: {solution.findPeakElement([1, 2, 4, 5, 7, 8, 3])}")