
from typing import List

"""
Intuition
The "Absolute Sum" of a subarray is either its maximum positive sum or absolute value of its minimum negative sum.
Think of it this way:
    - If a subarray sums to 10, its absolute sum is 10.
    - If a subarray sums to -15, its absolute sum is 15.

To find the largest possible absolute sum, we just need to track two things simultaneously as we walk through the array: the most positive a subarray can get and the most negative it can get. The answer will be the larger of the two magnitudes.

Approach
We use a modified Kadane's Algorithm. Instead of just tracking the current_max, we also track a current_min.
We use a modified Kadane's Algorithm. Instead of just tracking the current_max we also track a current_min.
    1. Initialize max_so_far and min_so_far to 0.
    2. Initialize global_max and global_min to 0.
    3. Iterate through each num in nums:
        - For the Max: Add num to max_so_far. If it becomes negative reset to it 0 (because a subarray starting from the next element would be better than a negative prefix).
        - For the Min: Add num to min_so_far. If it becomes positive, reset it to 0 (because a subarray starting from the next element would be more negative than a positive prefix).
        - Update the global records for both.
    4. Return the maximum of global_max and abs(global_min).

TC: O(n) We perform a single pass through the array of length n. Each operation inside the loop (addition and comparison) is O(1).

SC: O(1) We only use a constant amount of extra space for our four tracking variables (max_sum, min_sum, current_max, current_min) regardless of the input size.
"""
class Solution:
    # LC: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0

        current_max = 0
        current_min = 0

        for num in nums:
            # Traditional Kadane's for maximum
            current_max += num
            if current_max < 0:
                current_max = 0
            max_sum = max(max_sum, current_max)

            # Adapted Kadane's for minimum
            current_min += num
            if current_min > 0:
                current_min = 0
            min_sum = min(min_sum, current_min)
        return max(max_sum, abs(min_sum))