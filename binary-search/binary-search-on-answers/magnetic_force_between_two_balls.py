from typing import List

"""
Intuition:
The goal is to maximize the minimum distance between any two balls.
    - If we try to place balls with a very large minimum distance d, we might not find enough baskets.
    - If we try with a very small distance d, it's easy to fit them.
    - This monotonic property (if d works, d - 1 also works) signals that
    we can Binary Search on the answer (the force/distance itself).

Approach:
Sorting: First, sort the position array. This allows us to place balls greedily from left to right.

Binary Search Range
    - Low: 1 (The smallest possible force).
    - High: (position[-1] - position[0]) // (m-1) (The theoretical maximum possible force if balls were perfectly spaced). Or simply position[-1].

The Feasible Function (canPlace)
To check if a distance mid is possible:
    1. Place the first ball in the first basket (position[0]).
    2. Iterate through the baskets and place the next ball only if the current basket's distance from the last placed ball is >= mid.
    3. If we place all m balls, mid is feasible.

Complexity Analysis:
-------------------
Time Complexity: O(N log N + N log D)
    - Sorting: O(N log N), where N is the number of baskets. Sorting is
      required to use a greedy approach for ball placement.
    - Binary Search: O(log D), where D is the maximum possible distance
      (max(position) - min(position)).
    - Feasible Function: O(N) because we iterate through the sorted
      positions once to check if a minimum force 'd' is possible.
    - Total: O(N log N + N log D). Given constraints (N=10^5, D=10^9),
      this is well within the time limit.

Space Complexity: O(1) or O(N)
    - The algorithm itself uses O(1) auxiliary space for variables.
    - However, the space complexity depends on the sorting algorithm
      implementation (e.g., Python's Timsort requires O(N) auxiliary space).
"""


class Solution:
    # LC: https://leetcode.com/problems/magnetic-force-between-two-balls/description/
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlace(force):
            # Greedy placement
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= force:
                    count += 1
                    last_pos = position[i]
                if count >= m:
                    return True
            return False

        # Binary search on the resulting force
        left = 1
        right = position[-1] - position[0]
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            if canPlace(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

solution = Solution()
print(f"LC Solution: {solution.maxDistance([1,2,3,4,7], 3)}")