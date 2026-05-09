from typing import List

"""
Intuition:
    Imagine the capacity of your ship.
        - If the capacity is extremely small (e.g., the weight of the smallest package), you will never finish in days.
        - If the capacity is extremely large (e.g., the sum of all packages), you finish in exactly 1 day. There is a sweet spot capacity where if you go any lower, you exceed the day limit, but if you go any higher, you're just carrying extra empty space. Because the relationship between capacity and Days Required is monotonic (as capacity increases, days required decreases or stays the same), we can binary search for that boundary.

Approach: Binary Search on Answer
Define the Search Space
low: The maximum weight of a single package (max(weights)). The ship must be able to carry the heaviest item, or it can't move at all.
high: The sum of all weights (sum(weights)). This is the capacity needed to ship everything in exactly 1 day.

The Greedy Validator (can_ship)
For a given capacity mid, we check if it’s possible to ship within days. We iterate through the weights and keep a running sum. If adding the next package exceeds mid, we "reset" the ship for a new day.

The Algorithm
Initialize left = max(weights) and right = sum(weights).

While left < right:
Calculate mid (the candidate capacity).
Run the greedy validator.
If we can ship within the day limit, mid might be the answer, but a smaller one might also work. So, right = mid.
If we cannot ship, mid is too small. We must increase capacity: left = mid + 1.
Return left.

Time Complexity: O(N x log(sigma weights))
    - N: We iterate through the entire weights array once inside the can_ship function.
    - log(sigma weights - max(weights)): This is the number of times we perform binary search within our range.

Space Complexity: O(1)
    - We only use a few variables for the pointers (left, right, mid) and the greedy check. We do not use any extra data structures that scale with input size.
"""


class Solution:
    # LC: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            ships_needed = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    ships_needed += 1
                    current_load = 0
                current_load += w
            return ships_needed <= days

        # Step 1: Define the search space
        left = max(weights)
        right = sum(weights)

        # Step 2: Binary search
        while left < right:
            mid = left + (right - left) // 2

            # Step 3: Greedy validator
            if can_ship(mid):
                # Try to find an even smaller valid capacity
                right = mid
            else:
                left = mid + 1

        return left

    # GFG: https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1
    def leastWeightCapacity(self, arr, D):
        # code here
        def can_ship(mid):
            ships_needed = 1
            current_load = 0

            for weight in arr:
                if current_load + weight > mid:
                    ships_needed += 1
                    current_load = 0
                current_load += weight

            return ships_needed <= D

        left = max(arr)
        right = sum(arr)

        while left < right:
            mid = left + (right - left) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left

solution = Solution()
print(f"GFG Solution: {solution.leastWeightCapacity([1,2,3,4,5,6,7,8,9,10], 5)}")
print(f"LC Solution: {solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)}")