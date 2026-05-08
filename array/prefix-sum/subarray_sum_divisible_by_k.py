from typing import List

"""
Intuition: The goal is to find subarrays where Sum(i, j) (mod k) = 0. A subarray sum from index i to j can be expressed as the difference between two prefix sums:
Sum(i, j) = prefixsum[j] - prefixsum[i-1]
For this sum to be divisible by k:
(prefixsum[j]-prefixsum[i-1]) (mod k) = 0
-> prefixsum[j] (mod k) = prefixsum[i-1] (mod k)

The Core Insight: If two prefix sums have the same remainder when divided by $k$, the elements between them must sum to a multiple of k.

Approach: Hash Map + Prefix Sum
We iterate through the array once, keeping track of the running prefix sum and its remainder modulo k.
1. Initialize a Hash Map: Store the frequency of remainders encountered so far.
    - Initialize it with {0:1} to account for the case where a prefix sum itself is directly divisible by k (a subarray starting from index 0).
2. Iterate through nums:
    - Update the running_sum.
    - Calculate the remainder: rem = running_sum % k.
    - Handle Negatives: In many languages (like Python), % can return a negative value. We normalize it using rem = (rem + k) % k to ensure it stays in the range [0, k-1].
3. Count subarrays
    - If rem is already in the map, it means we have found subarrays ending at the current index that are divisible by k. Add the current count of that remainder to your total result.
    - Increment the frequency of rem in the map.

Time Complexity: O(n)
- We perform a single pass through the array of length n.
- Hash map operations (insert/lookup) are O(1) on average.
- Total time complexity: O(n).

Space Complexity: O(min(n, k))
- We store the remainders in a hash map.
- The number of unique remainders is capped by k.
- However, if n < k, we will store at most n entries.
- Total space complexity: O(min(n, k))

Edge Cases:
- Empty/Single Element Arrays: The constraints say n >= 1, but always consider if n = 1 and nums[0] % k == 0.
- Negative Numbers: Crucial point. Explain how you handle (-1) % 5. In Python, this is 4, but in C++/Java it might be -1. Normalizing the (rem+k)%k is the safest way to show Senior level awareness.
- Large k: If k is very large (e.g., 10^9), a hash map is better than a fixed-size array to save space.
"""

class Solution:
    # Function to count the number of subarrays with a sum that is divisible by K
    # GFG: https://www.geeksforgeeks.org/problems/sub-array-sum-divisible-by-k2617/1
    def subCount(self, arr, k):
        # Your code goes here
        remainder_count = {0: 1}
        running_sum = 0
        count = 0

        for num in arr:
            running_sum += num
            remainder = running_sum % k

            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Map to store frequency of remainders: {remainder: count}
        remainder_map = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num

            # Calculate remainder and normalize for negative sums
            remainder = running_sum % k
            if remainder < 0:
                remainder += k

            # If this remainder has been seen before, it means the
            # subarray between the previous occurrence and here sums to a
            # multiple of k
            if remainder in remainder_map:
                count += remainder_map[remainder]
                remainder_map[remainder] += 1
            else:
                remainder_map[remainder] = 1

        return count

solution = Solution()
print(f"GFG Solution: {solution.subCount([4,5,0,-2,-3,1], 5)}")
print(f"LC Solution: {solution.subarraysDivByK([4,5,0,-2,-3,1], 5)}")