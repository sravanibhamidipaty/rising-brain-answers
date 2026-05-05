"""
TC: O(n) where n is the number of elements in the array
SC: O(1)
"""

from typing import List

class SolutionGFG:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here
        current_sum = 0
        smallest = float("inf")
        left = 0
        n = len(arr)

        for right in range(n):
            current_sum += arr[right]
            while left <= right and current_sum > x:
                smallest = min(smallest, right - left + 1)
                current_sum -= arr[left]
                left += 1
        return smallest if smallest != float("inf") else 0


class SolutionLC:
    def minSubArrayLen(self, x: int, arr: List[int]) -> int:
        smallest = float("inf")
        left = 0
        current_sum = 0
        n = len(arr)

        for right in range(n):
            current_sum += arr[right]

            while left <= right and current_sum >= x:
                smallest = min(smallest, right - left + 1)
                current_sum -= arr[left]
                left += 1

        return smallest if smallest != float("inf") else 0


solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.smallestSubWithSum( 51, [1, 4, 45, 6, 0, 19])}")
print(f"LC Solution: {solutionLC.minSubArrayLen(4, [1,4,4])}")