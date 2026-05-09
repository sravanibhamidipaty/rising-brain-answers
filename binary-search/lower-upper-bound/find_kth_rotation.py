from typing import List

"""
The Pythonic Way:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

The Optimal Approach: Triple Reversal
1. Reverse the entire array. (This puts the elements that need to be at the front roughly in the right area, but in reverse order).
2. Reverse the first k elements. (This fixes the order).
3. Reverse the remaining n-k elements (This fixes their order).
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/rotate-array/
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k > n

        # Helper function to reverse a portion of the array in-place
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1. Reverse the whole array
        reverse(0, n - 1)

        # 2. Reverse first k elements
        reverse(0, k - 1)

        # 3. Reverse the rest
        reverse(k, n - 1)
        return nums


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/rotation4723/1
    def findKRotation(self, arr):
        # code here
        left = 0
        right = len(arr) - 1

        # 1. Handle the case where the array is already sorted
        if arr[left] <= arr[right]:
            return 0

        while left <= right:
            mid = left + (right - left) // 2

            # 2. Add a boundary check for mid + 1 to avoid IndexError
            if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
                return mid + 1

            if arr[mid] >= arr[left]:
                left = mid + 1
            else:
                right = mid  # Stay on mid because it could be the pivot

        return left


solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"Solution LC: {solutionLC.rotate([1,2,3,4,5,6,7], 3)}")
print(f"Solution GFG: {solutionGFG.findKRotation([5, 1, 2, 3, 4])}")