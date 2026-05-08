from typing import List

"""
TC: O(log n) where n is the number of elements in the array
SC: O(1)
"""


class SolutionLCIterative:
    # LC: https://leetcode.com/problems/binary-search/
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


"""
TC: O(log n) where n is the number of elements in the array
SC: O(log n) where n is the number of elements in the array due to stack frame calls
"""


class SolutionLCRecursive:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_search(left, right):
            if left > right:
                return -1

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return recursive_search(mid + 1, right)
            else:
                return recursive_search(left, mid - 1)

        return recursive_search(0, len(nums) - 1)


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/binary-search-1587115620/1
    def firstSearch(self, arr, k):
        # Code Here
        left = 0
        right = len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                index = mid
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return index

solutionLCIterative = SolutionLCIterative()
solutionLCRecursive = SolutionLCRecursive()
solutionGFG = SolutionGFG()
print(f"LC Iterative Solution: {solutionLCIterative.search([1, 2, 3, 4, 5], 4)}")
print(f"LC Recursive Solution: {solutionLCRecursive.search([1, 2, 3, 4, 5], 4)}")
print(f"GFG Solution: {solutionGFG.firstSearch([1, 2, 3, 4, 5], 4)}")