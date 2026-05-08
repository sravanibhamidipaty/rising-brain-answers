
from typing import List

"""
The Strategy: To find the longest such subarray, we need to track
the first time we see every prefix sum.

1. Initialize: Create an empty Hash Map (dictionary) to store
{prefix_sum: index} and a variable max_len = 0.
2. Iterate: Loop through the array while maintaining a current_sum
3. Check for Zero: If current_sum itself becomes 0, the
entire array from index 0 to your current index has a
sum of zero. Update max_len.
4. Check the Map: If the current_sum is already in your
map, you've found a subarray that sums to zero! Calculate its
length: current_index - Map[current_sum].
    - Compare this length with max_leng and keep the larger one
    - Crucial: If the sum is already in Map, do not update it.
    We want the earliest possible index to maximize the distance.
5. Add to Map: If the current_sum is new, store it in the Map
with the current index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
    def maxLength(self, arr):
        # code here
        # Dictionary to store the first occurrence of each prefix sum
        # Format: {prefix_sum: index}
        prefix_sum = {}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(arr):
            current_sum += num

            # Case 1: If current_sum is 0, the subarray from index 0 to i sums to 0
            if current_sum == 0:
                max_len = i + 1

            # Case 2: If current_sum has been seen before, a zero-sum subarray exists
            elif current_sum in prefix_sum:
                length = i - prefix_sum[current_sum]
                max_len = max(max_len, length)

            else:
                prefix_sum[current_sum] = i

        return max_len


"""
Intuition: The Remainder Pattern
If you are asked to find a sum that is a multiple of
k, you are essentially looking for a subarray where:
Subarray Sum \equiv 0 (mod k)

The core mathematical trick here is the Remainder Theorem (or Pigeonhole Principle logic):
    - Suppose you have a running sum (prefix sum) at index i and another at index j.
    - If PrefixSum[i] % k == r and PrefixSum[j] % k == r, then the difference between these two sums (which represents the subarray between them) must have a remainder of 0 when divided by k.
    - Analogy: If you have $14 (14 (mod 6) = 2) and later you have $26 (26 (mod 6) = 2), the $12 you gained in between is a perfect multiple of 6.

2. Approach: Hash Map + Prefix Sum
We use a Hash Map to store the first time we see a specific remainder.
1. Initialize: Create a Hash Map to store {remainder: index}
2. The "Edge Case" Base: Initialize the map with {0:-1}. Why? If a prefix sum from the very beginning is a multiple of k, we need a "starting point" at index -1 to ensure the length is at least 2.
3. Iterate: Traverse the array while maintaining a running prefix_sum.
4. Modulo: For every element, update prefix_sum = (prefix_sum + nums[i]) % k.
5. Check:
    - If the remainder exists in the map: Check the distance between the current index and the stored index. If current_index - stored_index >= 2, return True.
    - If the remainder does NOT exist: Store the current index with that remainder. (Do not update it if it exists; we want the earliest possible index to maximize our chances of meeting the length requirement).

TC: O(n)
- We traverse the array exactly once (n steps).
- Hash Map looksup and insertions are O(1) on average.
- Therefore, the total time is linear.

SC: O(min(n, k))
- In the worst case, we store a new remainder in the map for every element in the array.
- However, there are only k possible remainder (0 to k-1).
- The space used is the smaller of the number of elements or the number of possible remainders.
"""
class SolutionLC:
    # LC: https://leetcode.com/problems/continuous-subarray-sum/
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Step 1: Initialize the hash map with the base case.
        # We store {remainder: first_index_seen}.
        # Remainder 0 at -1 handles cases where the prefix sum
        # itself is a multiple of k from the very start.
        remainder_map = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num

            # Step 2: Calculate the remainder relative to k
            remainder = running_sum % k

            # Step 3: Check if we have seen this remainder before
            if remainder in remainder_map:
                # If the subarray length (current index - first seen index) is >= 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Step 4: Only store the index if the remainder is new.
                # We want to keep the OLDEST index to maximize subarray length.
                remainder_map[remainder] = i
        return False

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.maxLength([15, -2, 2, -8, 1, 7, 10, 23])}")
print(f"LC Solution: {solutionLC.checkSubarraySum([23,2,4,6,7], 6)}")