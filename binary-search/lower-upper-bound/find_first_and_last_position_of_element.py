from typing import List

"""
Is the target guaranteed to exist in the list?
Can the list be empty?

TC: O(log n) due to binary search
SC: O (1) because I am just calling the binarySearch function twice with a flag not storing
anything
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binarySearch(isFirst):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    index = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        left_index = binarySearch(True)
        right_index = binarySearch(False)

        return [left_index, right_index]

    def find(self, arr, x):
        # code here
        def binarySearch(isFirst):
            left = 0
            right = len(arr) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == x:
                    index = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        left_index = binarySearch(True)
        right_index = binarySearch(False)

        return [left_index, right_index]

solution = Solution()
print(f"GFG Solution: {solution.find([5,7,7,8,8,10], 8)}")
print(f"LC Solution: {solution.searchRange([5,7,7,8,8,10], 8)}")