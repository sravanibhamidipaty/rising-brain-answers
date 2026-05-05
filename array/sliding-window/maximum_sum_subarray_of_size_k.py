"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from collections import Counter
from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
    def maxSubarraySum(self, arr, k):
        # code here
        maximum_sum = 0
        current_sum = 0
        left = 0
        n = len(arr)

        for right in range(n):
            current_sum += arr[right]

            while right - left + 1 > k:
                current_sum -= arr[left]
                left += 1

            if right - left + 1 == k:
                maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum


"""
TC: O(n) where n is the number of elements in the array
SC: O(k) where k is the given window size
"""

class SolutionLC:
    # LC: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums):
            return 0
        element_count = Counter(nums[:k])
        current_sum = sum(nums[:k])
        maximum_sum = current_sum if len(element_count) == k else 0
        n = len(nums)

        for i in range(k, n):
            element_count[nums[i]] = element_count.get(nums[i], 0) + 1
            element_count[nums[i - k]] -= 1

            if element_count[nums[i - k]] == 0:
                element_count.pop(nums[i - k])

            current_sum += nums[i] - nums[i - k]
            maximum_sum = (
                max(current_sum, maximum_sum)
                if len(element_count) == k
                else maximum_sum
            )

        return maximum_sum

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.maxSubarraySum([100, 200, 300, 400], 2)}")
print(f"LC Solution: {solutionLC.maximumSubarraySum([1,5,4,2,9,9,9], 3)}")