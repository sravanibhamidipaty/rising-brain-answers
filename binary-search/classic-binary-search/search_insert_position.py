from typing import List

"""
TC: O(log n) where n is the number of elements in the array
SC: O(1) because only using 3 variables no additional data structures
"""


class Solution:
    # LC: https://leetcode.com/problems/search-insert-position/
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # GFG: https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1
    def searchInsertK(self, arr, k):
        # code here
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid
        return left

solution = Solution()
print(f"GFG Solution: {solution.searchInsertK([1,3,5,6], 2)}")
print(f"LC Solution: {solution.searchInsert([1,3,5,6], 2)}")