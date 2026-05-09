from math import ceil
from typing import List

"""
Intuition
The core challenge is finding the minimum integer speed to satisfy a deadline.
    - Monotonicity: If a speed v allows you to arrive on time, any speed greater than v will also allow you to arrive on time. Conversely, if v is too slow, any speed less than v is definitely too slow.
    - Search Space: This Yes/No threshold behavior is the class indicator for Binary Search Over the Answer. Instead of trying to calculate the speed directly, we "guess" a speed and check if it's feasible.

Approach
    - We implement a binary search within the range of possible speeds [1, 10**7].
    - Boundary Case: Each of the first n-1 trains requires at least 1 hour (because you must wait for an integer hour to depart). If the total hour <= n-1, it is mathematically impossible to reach the office. We return -1.
    - The Check Function (isPossible):
        - For each train i from 0 to n-2: the time taken is [dist[i]/speed].
        - For the last train: the time taken is exactly dist[n-1]/speed (no waiting).
        - Return True if the sum of these times <= hour.
    - Binary Search Logic:
        - If isPossible(mid) is true: mid might be the answer, but we want the minimum, so we look left (right = mid - 1).
        - If isPossible(mid) is false: we must go faster, so look right (left = mid + 1).

Time Complexity
    - Binary Search Range: Let K be the range of possible speeds (here, 10**7). The search takes O(log K) iterations.
    - Feasibility Check: In each iteration, we iterate through the dist array of size N once.
    - Total Complexity: O(N log K)
        - Given N = 10**5 and K = 10**7, log_base(2) ~ 24. Total operations ~ 2.4x10^6, which comfortably fits within the 1-second limit.

Space Complexity
    - Space: O(1)
        - We only use a few constant variables (left, right, total_time) regardless of the input size. No extra data structures or recursive stacks are required.
"""


class Solution:
    # LC: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        def can_reach_on_time(speed):
            total_time = 0

            # All trains except the last one require waiting for the next integer hour
            for i in range(len(dist) - 1):
                total_time += ceil(dist[i] / speed)

            # The last train does not require a wait
            total_time += dist[-1] / speed
            return total_time <= hour

        left = 1
        right = 10**7

        while left < right:
            mid = left + (right - left) // 2
            if can_reach_on_time(mid):
                right = mid  # Because right can be the pivot
            else:
                left = mid + 1

        return left
