"""
Intuition: O(n^3) 3 nested for loops

Approach: O(n^2) with sorting and 3 points

TC: O(n^2) n for the for loop and n for the while loop where n is the number of elements in nums

SC: O(1) because of .sort() in place
"""

from typing import List

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1
    def hasTripletSum(self, nums, target):
        # Code Here
        if not nums:
            return False

        if len(nums) < 3:
            return False

        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    return True
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
        return False


"""
Questions to ask:
can there be no valid solutions?
can length of nums be less than 3?

TC: O(n^2)
SC: O(n^2) in the absolute worst case for the 3Sum problem, the number of valid triplets can be quadratic relative to the number of elements in the input array. For an array of size n, there can be up to O(n^2) unique triplets that sum to zero.

The perfect interview answer:
The time complexity is O(n^2) because we iterate through the array and use a two-pointer approach for each element. The space complexity is O(n^2) if we include the output, as there can be up to O(n^2) unique triplets. However, the auxiliary space--excluding the result--is O(1) beyond the space required for the sorting algorithm.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/3sum/
    """
    Questions to ask:
    can there be no valid solutions?
    can length of nums be less than 3?

    TC: O(n^2)
    SC: O(n^2) in the absolute worst case for the 3Sum problem, the number of valid triplets can be quadratic relative to the number of elements in the input array. For an array of size n, there can be up to O(n^2) unique triplets that sum to zero.

    The perfect interview answer:
    The time complexity is O(n^2) because we iterate through the array and use a two-pointer approach for each element. The space complexity is O(n^2) if we include the output, as there can be up to O(n^2) unique triplets. However, the auxiliary space--excluding the result--is O(1) beyond the space required for the sorting algorithm.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) < 3:
            return []

        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1

        return result

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.hasTripletSum([1, 4, 45, 6, 10, 8], 13)}")
print(f"Leetcode Solution: {solutionLC.threeSum([-1,0,1,2,-1,-4])}")