import heapq

"""
Kadane's Algorithm is great for finding the single maximum 
subarray sum, but it won't work for finding the K-th larges
among all possible subarrays.

Since the problem asks for the K-th largest out
of all possible contiguous subarrays, and the constraints
(N <= 1000) allow for an O(N^2 log K) approach, here is the
standard way to solve it:

The Logic
1. Generate all subarray sums: Use nested loops to calculate
the sum of every possible contiguous subarray.
2. Maintain a Min-Heap of size K: *Push sums into the heap.
    - If the heap size exceeds K, pop the smallest element.
3. Result: After checking all subarrays, the top of the min-heap
will be the K-th largest sum.

Time Complexity: O(N^2 * log K)
- We iterate through all possible contiguous subarrays using nested loops, 
  which takes O(N^2) time.
- For each subarray sum generated, we perform a heap push and potentially 
  a heap pop operation. 
- Since the min-heap is maintained at a maximum size of K, each heap 
  operation costs O(log K).
- Total complexity: O(N^2) subarrays * O(log K) heap adjustment.

Space Complexity: O(K)
- We maintain a min-heap to store the top K largest subarray sums encountered.
- While some resources might cite O(log K) for internal heap tree height, 
  the actual memory allocation for the data structure is proportional 
  to the number of elements stored, which is K.
- Variable overhead (pointers and running sums) is O(1).
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1
    def kthLargest(self, arr, k) -> int:
        # code here
        n = len(arr)
        min_heap = []

        # Iterate through all possible starting points
        for i in range(n):
            current_sum = 0
            # Iterate through all possible ending points for
            # the current start
            for j in range(i, n):
                current_sum += arr[j]

                # Maintain only the top Kth-largest sums in
                # the min-heap
                heapq.heappush(min_heap, current_sum)

                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

solution = Solution()
print(f"GFG Solution: {solution.kthLargest([3, 2, 1], 2)}")