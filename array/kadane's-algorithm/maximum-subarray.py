"""
TC: O(n) where n is the number of elements in the array
SC: O(1) because I am not using any additional data structures
"""

from typing import List

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
    def maxSubarraySum(self, arr):
        # Code here
        max_sum = float("-inf")
        current_sum = 0

        for num in arr:
            current_sum += num
            current_sum = max(current_sum, num)
            max_sum = max(current_sum, max_sum)
        return max_sum

    # LC: https://leetcode.com/problems/maximum-subarray/
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum += num
            current_sum = max(current_sum, num)
            max_sum = max(max_sum, current_sum)

        return max_sum

solution = Solution()
print(f"GFG Solution: {solution.maxSubarraySum([-2,1,-3,4,-1,2,1,-5,4])}")
print(f"LC Solution: {solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])}")