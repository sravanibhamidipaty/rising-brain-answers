"""
TC: O(log n)
Binary Search: You are using two separate binary search calls (binarySearch(True) and binarySearch(False)). Each call narrows the search range by half in every iteration.
Calculations: Since each call takes O(log n) and they are executed sequentially, the total time is O(log n) + O(log n) = O(2 log n), which simplifies to O(log n).

SC: O(1)
Iterative Approach: You are using a while loop rather than recursion.
Variable Usage: You only allocate a few integer variables (left, right, mid, index) regardless of how large the input array arr grows.
In-place: You are not creating any additional data structures (like lists or hash maps) that scale with the input size. Thus, it is O(1) (constant space).
"""
class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
    def countFreq(self, arr, target):
        # code here
        def binarySearch(isFirst):
            left = 0
            right = len(arr) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == target:
                    index = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        left_index = binarySearch(True)

        if left_index == -1:
            return 0
        right_index = binarySearch(False)

        return right_index - left_index + 1

solution = Solution()
print(f"GFG Solution: {solution.countFreq([1, 1, 2, 2, 2, 2, 3], 2)}")