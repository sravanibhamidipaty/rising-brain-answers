"""
Can nums have no ones?
Can nums be empty?

TC: O(n) where n is the number elements in nums
SC: O(1) because I am using pointers and variables
"""

from typing import List

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1
    def maxOnes(self, arr, k):
        # code here
        left = 0
        longest = 0
        num_zeros = 0
        n = len(arr)

        for right in range(n):
            if arr[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if arr[left] == 0:
                    num_zeros -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest

    def longestOnes(self, nums: List[int], k: int) -> int:
        # LC: https://leetcode.com/problems/max-consecutive-ones-iii/description/
        maxx = 0
        left = 0
        n = len(nums)
        num_zeros = 0

        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1

            if num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            maxx = max(right - left + 1, maxx)
        return maxx

solution = Solution()
print(f"GFG Solution: {solution.maxOnes([1,1,1,0,0,0,1,1,1,1,0], 2)}")
print(f"LC Solution: {solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)}")