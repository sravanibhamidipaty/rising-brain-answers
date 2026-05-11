"""
Intuition:
The goal is to maximize the minimum distance.
    - If we try to place cows with a very small minimum distance
    (e.g. d = 1), it's very easy to fit them all.
    - If we try a very large distance (e.g. d=10^8), it's impossible.
    - There is a specific threshold: for any distance <= X, we can
    place k cows; for any distance > X, we cannot.

Since this property is monotonic (if d works, d-1 also works),
we can use Binary Search to find the largest d that satisfies
the condition.

Approach:
Step 1: Sort the Stalls
    - To greedily place cows, we must know the positions in order.
    stalls.sort()

Step 2: Define the Search Space
    - Low (low): The smallest possible distance, which is 1.
    - High (high): The maximum possible distance, which is:
    stalls[n-1] - stalls[0].

Step 3: The "Can Place" Helper Function
We need a function canPlace(distance) that returns True if we
can place k cows such that every pair is at least distance
apart.
    1. Place the first cow in the first stall stalls[0].
    2. Iterate through the rest of the stalls. If the
    current stall is at least distance away from the last
    place cow, place the next cow there.
    3. If we place >= k cows, return True.

Step 4: Binary Search Logic
While low <= high:
    - Calculate mid = low + (high-low)//2
    - If canPlace(mid) is True:
        - This distance works! But there might be a larger one.
        Save mid and move low = mid + 1
    - Else:
        - This distance is too large. Move high = mid-1.

Time Complexity
    - Sorting: O(N log N), where N is the number of stalls.
    - Binary Search: The range of the search is D = (max_pos - min_pos).
    This takes O(log D) steps.
    - Helper Function: In each binary search step, we traverse the stalls once,
    which is O(N).
    - Total O(N log N + N log D). Given the constraints, this fits comfortably
    within the time limit.

Space Complexity
    - O(1) (or O(N) depending on the sorting algorithm's implementation),
    as we only use a few variables for the search.
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/aggressive-cows/1
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()

        def canPlace(distance):
            count = 1
            last_pos = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= distance:
                    count += 1
                    last_pos = stalls[i]
                if count >= k:
                    return True
            return False

        low = 1
        high = stalls[-1] - stalls[0]
        res = 0

        while low <= high:
            mid = low + (high - low) // 2

            if canPlace(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res

solution = Solution()
print(solution.aggressiveCows([1, 2, 4, 8, 9], 3))  # Output: 3