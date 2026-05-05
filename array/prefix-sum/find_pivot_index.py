
from typing import List

"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

class SolutionBF:
    def findEquilibrium(self, arr):
        # code here
        n = len(arr)
        prefix_sum = [0] * n
        postfix_sum = [0] * n

        prefix = 0
        for i in range(n):
            prefix_sum[i] += prefix
            prefix += arr[i]

        postfix = 0
        for i in range(n - 1, -1, -1):
            postfix_sum[i] += postfix
            postfix += arr[i]

        for i in range(n):
            if prefix_sum[i] == postfix_sum[i]:
                return i

        return -1


"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

class SolutionO:
    # GFG: https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1#approach-3-using-two-pointers-on-time-and-on-space
    # LC: https://leetcode.com/problems/find-pivot-index/description/
    def equilibriumPoint(self, arr: List[int]):
        prefSum = 0
        total = sum(arr)

        # Iterate pivot over all the elements of the
        # array and till prefSum != suffSum

        for pivot in range(len(arr)):
            suffSum = total - prefSum - arr[pivot]
            if prefSum == suffSum:
                return pivot
            prefSum += arr[pivot]

        return -1