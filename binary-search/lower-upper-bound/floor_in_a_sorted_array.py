"""
Time Complexity (TC): O(log n) Because you are halving the search space in each iteration of the while loop, the number of steps required to find the element is logarithmic relative to the size of the array.
Space Complexity (SC): O(1) You are only using a constant amount of extra space for variables (left, right, index, and mid), regardless of how large the input array grows.
"""

class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
    def findFloor(self, arr, x):
        # code here
        left = 0
        right = len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] <= x:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index
