"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1
    def countSubArrayProductLessThanK(self, arr, n, k):
        left = 0
        count = 0
        product = 1

        for right in range(n):
            product *= arr[right]
            while left <= right and product >= k:
                product //= arr[left]
                left += 1
            count += right - left + 1

        return count

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # LC: https://leetcode.com/problems/subarray-product-less-than-k/
        product = 1
        left = 0
        n = len(nums)
        count = 0

        for right in range(n):
            product *= nums[right]

            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1
        return count


solution = Solution()
print(f"GFG Solution: {solution.countSubArrayProductLessThanK([1, 2, 3, 4], 4, 10)}")
print(f"LC Solution: {solution.numSubarrayProductLessThanK([10,5,2,6], 100)}")