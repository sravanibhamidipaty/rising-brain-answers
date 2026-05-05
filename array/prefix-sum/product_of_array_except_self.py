from typing import List

"""
2-3 cases:
Can the array be empty or only one element.
Array size

Intuition:
Nested for loops i from 0, len(nums) and j from 0, len(nums) and multiply everything
except when i == j.
TC: O(n^2)
SC: O(1)

Approach:
Final result array
Prefix of all the number before the current number stored in the result array
Suffix of all the number before the current number stored in the result array
Return result
TC: O(n) Loop through the array twice but in separate for loops one for prefix and
one for suffix
SC: O(1) without considering the result array

nums = [1, 2, 3, 4]
result = [1] * len(nums) = [1, 1, 1, 1]
prefix = 1
iteration 0: result = [1, 1, 1, 1], prefix = 1
iteration 1: result = [1, 1, 1, 1], prefix = 2
iteration 2: result = [1, 1, 2, 1], prefix = 6
iteration 3: result = [1, 1, 2, 6], prefix = 24

postfix = 1
nums = [1, 2, 3, 4]
Start the for loop from len(nums)-1
iteration 3: result = [1, 1, 2, 6], postfix = 4
iteration 2: result = [1, 1, 8, 6], postfix = 12
iteration 1: result = [1, 12, 8, 6], postfix = 24
iteration 0: result = [24, 12, 8, 6], postfix = 24
"""


class Solution:
    # LC: https://leetcode.com/problems/product-of-array-except-self/description/
    def productExceptSelfLC(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    # GFG: https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1
    def productExceptSelfGFG(self, arr):
        # code here
        n = len(arr)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= arr[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= arr[i]

        return result

solution = Solution()
print(f"GFG Solution: {solution.productExceptSelfLC([10, 3, 5, 6, 2])}")
print(f"LC Solution: {solution.productExceptSelfGFG([10, 3, 5, 6, 2])}")