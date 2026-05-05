from typing import List

"""
Questions:
Can nums be empty?
Can nums be only one number?
Does nums contain negative numbers?

Intuition:
Have a hashmap that counts the sum. If current_sum-k in counter, then that += 1 and total += counter[current_sum-k]
return total

Time Complexity: O(n) where n is the total number of elements in the array because I need to loop through nums
Space Complexity: O(n) where n is the total number of elements in the array if all sum numbers are unique
"""


class Solution:
    # LC: https://leetcode.com/problems/subarray-sum-equals-k/description/
    def subarraySum(
        self, nums: List[int], k: int
    ) -> int:  # nums = [1, -1, 1, 1, 1], k = 2
        # current_sum = 0
        # prefix_sum = {0:1}
        # result = 0

        # for num in nums: # 1 / -1 / 1 / 1 / 1
        #     current_sum += num # 1 / 0 / 1 / 2 / 3
        #     result += prefix_sum.get(current_sum-k, 0) # 0 / 0 / 0 / 1 / 2
        #     prefix_sum[current_sum] = prefix_sum.get(current_sum, 0)+1 # {0:1, 1:1} / {0:2, 1:1} / {0:2, 1:2} / {0:2, 1:2, 2:1} / {0:2, 1:2, 2:1, 3:1}
        # return result # 2

        current_sum = 0
        prefix_sum = {0: 1}
        result = 0

        for num in nums:
            current_sum += num
            result += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return result

    def cntSubarrays(self, arr, k):
        # code here
        # GFG: https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1
        prefix_sum = {0: 1}
        current_sum = 0
        result = 0

        for num in arr:
            current_sum += num
            result += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return result

solution = Solution()
print(f"GFG Solution: {solution.cntSubarrays([10, 2, -2, -20, 10], -10)}")
print(f"LC Solution: {solution.subarraySum([1,1,1], 2)}")