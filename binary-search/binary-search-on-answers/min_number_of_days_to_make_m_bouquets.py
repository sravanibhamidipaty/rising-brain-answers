from typing import List

"""
Intuition
In a standard binary search, you look for a number in a sorted
list. In Binary Search on Answer, you look for a threshold in
a range of possible values.

Imagine a timeline from Day 1 to Day 10**9.
    - On Day 1, maybe no flowers have bloomed.
    Result: False (cannot make m bouquets).
    - On Day 10**9, all flowers have bloomed.
    Result: True (can definitely make m bouquets).
    - There is a specific day D where the answer switches
    from False to True. Because this relationship is montonic
    (if you can do it on Day D, you can do it on Day D + 1),
    you can binary search for that switch point.

Approach
The Search (Binary Search)
    - Low: min(arr) (The earliest any flower blooms).
    - High: max(arr) (The latest any flower blooms).
    - Mid A trial day.
    - If check(mid) is true, mid could be the answer, but
    there might be a smaller day that also works. So, we
    record mid and try a smaller range (high = mid - 1).
    - If check(mid) is false, we need more time.

The Validator (Greedy Check)
This is where the adjacency constraint from Minimum days to
make M bouquets is handled.
    - Traverse the original arr linearly.
    - Keep a counter of consecutive_bloomed flowers.
    - If a flower's bloom day <= current trial day:
        consecutive_bloomed += 1
    - If consecutive_bloomed == k: You just made a bouquet!
    Increment total_bouquets and reset consecutive_bloomed = 0.
    - If a flower hasn't bloomed yet: Rest consecutive_bloomed = 0
    (adjacency is broken).

Complexity Analysis
Let N be the number of flowers and W be the range of days
(max(arr)-min(arr)).

Time Complexity: O(N x log(W))
    - log(W): The binary search halves range of days each
    time. With a range up to 10**9, this is only about 30
    iterations.
    - N: Inside each iteration, we perform a single linear
    scan of the array to count bouquets.
    - Total: O(N x log(max_element)), which is highly efficient

Space Complexity: O(1)
    - We only store a few variables (low, high, mid, count, bouquets).
    - We do not modify the input array or create new DS.
"""

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1
    def minDaysBloom(self, arr, k, m):
        # Code here
        def canMake(day):
            bouquets = 0
            flowers = 0

            for bloom_day in arr:
                if bloom_day <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0  # Reset because adjacency is broken

            return bouquets >= m

        left = min(arr)
        right = max(arr)
        res = -1

        while left <= right:
            mid = left + (right - left) // 2

            if canMake(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

    # LC: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMake(day):
            bouquets = 0
            flowers = 0

            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if canMake(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

solution = Solution()
print(f"GFG Solution: {solution.minDaysBloom([1, 10, 3, 10, 2], 1, 3)}")  # Output: 3
print(f"LC Solution: {solution.minDays([1, 10, 3, 10, 2], 3, 1)}")  # Output: 3