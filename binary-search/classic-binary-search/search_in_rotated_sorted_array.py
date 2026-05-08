from typing import List

"""
Can the array be empty?
Possibly left rotated -> can it not be rotated? Yes

Intuition:
Linear search and see if target is at each index of the number -> TC: O(n), SC: O(1)

Approach:
Sorted array -> TC: O(log n) -> Binary search -> SC: O(1)
2 pointers: left starts at the beginning of the nums array and right starts at the
end of the nums array.
Find the mid value and see which half of the array is sorted:
if nums[left] <= nums[mid] -> Left half is sorted
if nums[left] <= target < nums[mid] -> right = mid - 1
else -> left = mid + 1
else -> Right half is sorted
if nums[mid] <= target <= nums[right] -> left = mid + 1
else -> right = mid - 1

nums = [4,5,6,7,0,1,2]
left = 0, right = 6, mid = 3. nums[left] = 4 < nums[mid] = 7 left half is sorted
4 <= 0 < 7 No
left = 3+1 = 4
left = 4, right = 6, mid = 5. nums[left] = 0 < nums[mid] = 1 left half is sorted
nums[left] = target return 4
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

solution = Solution()
print(f"Solution: {solution.search([4,5,6,7,0,1,2], 0)}")