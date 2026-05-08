from typing import List

"""
Intuition: The trick here is that a product is different from a sum because two negative numbers make a positive. If you only track the maximum product so far (as you would in Kadane's for sums), you lose the potential of a very small negative number becoming a very large positive number when multiplied by another negative. Therefore, you must track both the running maximum and the running minimum.

Approach:
Initialization: Start your current_max, current_min, and result with the first element of the array.

Iteration: Loop through the array starting from the second element.

The Swap/Reset: At each element n:
    1. If n is negative, the maximum product could become the minimum and vice versa.
    2. Update current_max by taking the maximum of three things: the current element n, the product n * current_max, or the product n*current_min.
    3. Update current_min similarly.

Global Max: Update your result at each step

TC: O(n). We perform a single pass through the array, making it highly efficient for large datasets.
SC: O(1). We only store three variables (res, max_so_far, min_so_far), regardless of the input size.

Why this works for Edge Case
- Zeros: If the current element is 0, both max_so_far and min_so_far will reset to 0. The algorithm then effectively "restarts" from the next element, which is correct for subarrays.
- Negative Numbers: By keeping the min_so_far, we carry the largest negative product, waiting for another negative number to flip it back into a large positive value.
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
    def maxProductGFG(self, arr):
        # code here
        res = max_so_far = min_so_far = arr[0]

        n = len(arr)

        for i in range(1, n):
            temp_max = max(arr[i], max_so_far * arr[i], min_so_far * arr[i])
            min_so_far = min(arr[i], max_so_far * arr[i], min_so_far * arr[i])
            max_so_far = temp_max
            res = max(max_so_far, res)

        return res

    # LC: https://leetcode.com/problems/maximum-product-subarray/
    def maxProductLC(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize with the first element
        res = max_so_far = min_so_far = nums[0]

        for i in range(1, len(nums)):
            # Temporary storage to prevent using the updated max_so_far
            # when calculation the new min_so_far
            temp_max = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
            min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)

            max_so_far = temp_max

            # Update the global result
            res = max(max_so_far, res)

        return res

solution = Solution()
print(f"GFG Solution: {solution.maxProductGFG([-2, 6, -3, -10, 0, 2])}")
print(f"LC Solution: {solution.maxProductLC([-2, 6, -3, -10, 0, 2])}")