from math import ceil
from typing import List
"""
Clarifying Questions
    - Is it guaranteed that h is at least the number of piles? (If h < piles.length, it's impossible because she can only eat from one pile per hour).
    - What is the range of h and the number of bananas in each pile? (Knowing they can be up to 10^9 tells me a linear search will be too slow).
    - If Koko finishes a pile in less than an hour, can she start another pile in the same hour? (The problem says no, she waits until the next hour).

Intuition
    - Initial thought: We are looking for a value k.
        - If k is very small (1), Koko might take too long.
        - If k is very large (the maximum value in piles), she will finish in exactly piles.length hours.
    - As k increases, the time taken to eat all bananas monotonically decreaseas. This monotonic property suggests we can use Binary Serach on the answer space of k.
    The range: low (1) minimum possible speed. high: max(piles) (maximum possible speed needed).

Approach:
1. Define a helper function can_finish(speed) that calculates the total hours needed for a given speed k. For each pile, hours needed = ceil(pile / k).
2. Perform binary search on the range [1, max(piles)]
3. If can_finish(mid) is true, mid could be the answer, but we try to find a smaller speed by moving high = mid.
4. If can_finish(mid) is false, the speed is too slow, so we move low = mid + 1.

Time Complexity: O(N * log M), where N is the number of piles and M is the maximum number of bananas in a pile.
    - The binary search takes log(M) steps.
    - In each step, we iterate through N piles to check if the speed works.
Space Complexity: O(1) as we only store a few variables for the binary search.

Dry Run (Example 1)
Input: piles = [3, 6, 7, 11], h = 8
Range: low = 1, high = 11
Mid = 6:
    - Hours: ceil(3/6)=1, 6/6=1, 7/6=2, 11/6=2 -> Total 6 hours.
    - 6 <= 8? Yes. Speed 6 works, try smaller. high = 6.

Mid = 3
    - Hours: ceil(3/3)=1, 6/3=2, 7/3=3, 11/3=4 -> Total = 10 hours.
    - 10 <= 8? No. Speed 3 does not work, try higher. low = 3+1 = 4

Mid = 4
    - Hours: ceil(3/4)=1, 6/4=2, 7/4=2, 11/4=3. Total = 6 hours.
    - 6 <= 8. Yes. Speed 4 works, try smaller. high = 4

Result low meets high at 4.
"""


class Solution:
    # LC: https://leetcode.com/problems/koko-eating-bananas/
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(mid):
            total = 0
            for pile in piles:
                total += ceil(pile / mid)
            return total <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left

    # GFG: https://www.geeksforgeeks.org/problems/koko-eating-bananas/1
    def kokoEat(self, arr, k):
        # Code here
        def can_finish(s):
            total = 0

            for pile in arr:
                total += ceil(pile / s)

            return total <= k

        left = 1
        right = max(arr)

        while left < right:
            mid = left + (right - left) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left

solution = Solution()
print(f"GFG Solution: {solution.minEatingSpeed([5, 10, 3], 4)}")
print(f"LC Solution: {solution.minEatingSpeed([3,6,7,11], 8)}")