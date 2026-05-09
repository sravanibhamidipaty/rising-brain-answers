"""
Time Complexity (TC): O(log n) You are using Binary Search. In each iteration of the while loop, you divide the search space (the distance between left and right) in half.
For an array of size n, this takes at most log_2 n steps.
Space Complexity (SC): O(1) You are only using a few integer variables (left, right, mid, index) regardless of how large the input array is.
Since you aren't using recursion (which would add to the call stack) or any additional data structures, the auxiliary space remains constant.
"""

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1
    def findCeil(self, arr, x):
        # code here

        left = 0
        right = len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] >= x:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        return index

solutionGFG = Solution()
print(f"GFG Solution: {solutionGFG.findCeil([1, 2, 8, 10, 11, 12, 19], 5)}")