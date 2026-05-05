"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1
    def totalElements(self, arr):
        # Code here
        longest = 0
        counter = {}
        left = 0
        n = len(arr)

        for right in range(n):
            counter[arr[right]] = counter.get(arr[right], 0) + 1

            while left <= right and len(counter) > 2:
                counter[arr[left]] -= 1
                if counter[arr[left]] == 0:
                    counter.pop(arr[left])
                left += 1

            longest = max(
                longest, right - left + 1
            )  # The key is at most two distinct integers

        return longest

    def totalFruit(self, arr: List[int]) -> int:
        # LC: https://leetcode.com/problems/fruit-into-baskets/
        longest = 0
        left = 0
        n = len(arr)
        counter = {}

        for right in range(n):
            counter[arr[right]] = counter.get(arr[right], 0) + 1

            while left <= right and len(counter) > 2:
                counter[arr[left]] -= 1
                if counter[arr[left]] == 0:
                    counter.pop(arr[left])
                left += 1
            longest = max(longest, right - left + 1)
        return longest

solution = Solution()
print(f"GFG Solution: {solution.totalElements([2, 1, 2])}")
print(f"LC Solution: {solution.totalFruit([2, 1, 2])}")