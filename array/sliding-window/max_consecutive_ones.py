"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/max-consecutive-one/1
    def maxConsecBits(self, arr):
        # code here
        if not arr or len(arr) == 1:
            return len(arr)

        count = 1
        maxx = 0
        n = len(arr)

        for i in range(1, n):
            if arr[i - 1] != arr[i]:
                maxx = max(count, maxx)
                count = 1
            else:
                count += 1

        return max(maxx, count)

"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

class SolutionLC:
    # LC: https://leetcode.com/problems/max-consecutive-ones/
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                maxx = max(count, maxx)
                count = 0
        return max(maxx, count)

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.maxConsecBits([0, 1, 0, 1, 1, 1, 1])}")
print(f"LC Solution: {solutionLC.findMaxConsecutiveOnes([1,1,0,1,1,1])}")