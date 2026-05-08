from typing import List

"""
Intuition: In a linear array, the maximum subarray is simply a contiguous segment. In a circular array, the maximum subarray can take two forms:
    1. The Non-Circular Case: The maximum subarray stays within the array boundaries (Standard Kadane's).
    2, The Circular Case: The maximum subarray "wraps around" the end to the beginning.

The Key Insight: If the maximum subarray wraps around, the elements it excludes must form a contiguous minimum subarray in the middle of the array.

Therefore:
Max Circular Sum = Total Array Sum - Minimum Subarray Sum

Approach
We can calculate both the maximum subarray sum and the minimum subarray sum in a single pass using a modified version of the standard Kadane's pattern.
1. Standard Kadane's: Find the max_sum (standard maximum subarray).
2. Inverse Kadane's: Find the min_sum (standard minimum subarray).
3. Total Sum: Keep track of the total_sum of the array.
4. Edge Case: If all numbers are negative, the total_sum-min_sum will result in 0 (an empty subarray), which is not allowed. In this case, we must return the max_sum (which would be the least negative number).
5. Final Result: Return max(max_sum, total_sum-min_sum).
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1
    # LC: https://leetcode.com/problems/maximum-sum-circular-subarray/
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Standard Kadane variables
        max_sum = float("-inf")
        current_max = 0

        # Min-Kadane variables
        min_sum = float("inf")
        current_min = 0

        total_sum = 0

        for num in nums:
            total_sum += num

            # Standard Kadane (Max Subarray)
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            # Inverse Kadane (Min Subarray)
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        # If max_sum is negative, all elements are negative
        # Return max_sum because total_sum - min_sum would be 0 (empty)
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)
