from typing import List

"""
Intuition
The original array is strictly increasing, then rotated, so it is made of two sorted segments with a “pivot” where the order drops.​

The minimum is exactly that pivot element: the first element that is smaller than everything before it.

Because the array is mostly sorted and the problem asks for better than linear scan, this strongly suggests binary search on the structure of the array.​

Approach
Maintain two pointers: left = 0, right = n - 1.

If the array is not rotated (i.e., nums[left] < nums[right]), then nums[left] is already the minimum; return it immediately.​

While left < right:

Compute mid = (left + right) // 2.

Compare nums[mid] with nums[right]:

If nums[mid] > nums[right], the minimum must be in the right half (excluding mid), so set left = mid + 1.

Otherwise (nums[mid] <= nums[right]), the minimum lies in the left half including mid, so set right = mid.

When the loop ends, left == right and that index points to the minimum; return nums[left].​

Key phrase to say: “I’m using binary search on the shape of the rotated sorted array, comparing mid to the rightmost element to decide which half still contains the rotation pivot (and thus the minimum).”​

Time Complexity
Each step halves the search space using binary search, so time is O(log n).​

Space Complexity
Uses only a few pointers and variables; extra space is O(1).
"""


class Solution:
    # LC: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

   # GFG: https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1
    def findMin(self, arr):
        # code here
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return arr[left]

solution = Solution()
print(f"Solution: {solution.findMin([3, 1, 2])}")