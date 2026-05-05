"""
Goal: For each element in the array, we find the maximum level of
water it can trap after the rain, which is equal to the minimum
of maximum height of bars on both the sides minus its own height.

Algorithm:
- Initialize ans = 0
- Iterate the array from left to right:
    - Initialize left_max = 0 and right_max = 0
    - Iterate from the current element to the beginning of array updating:
        - left_max = max(left_max, height[j])
    - Iterate from the current element to the end of array updating:
        - right_max = max(right_max, height[j])
    - Add min(left_max, right_max) - height[i] to ans

Clarification & Edge Cases
    - What are the constraints on n? (The page says up to 2 x 10^4, which suggests an O(n) or O(n log n) solution).
    - Can the input be empty or have fewer than 3 bars? If the array length is < 3, no water can be trapped.
    - What is the maximum height? If heights are very large, we must ensure our sum doesn't overflow (though with 10^5, a standard integer is fine).
    - Are there any negative heights? (The problem says non-negative, but it's good to confirm).

Intuition
The core idea is: How much water can be trapped on top of a single bar at index i?
Water is trapped at index i only if there is a taller bar to its left and a taller bar to its right. The height of the water at i is determined by the shorter of the two tallest bars on either side, minus the height of the bar itself: Water at i = min(max_left_i, max_right_i).

Approaches
A. Brute Force (Conceptual)
For every element, we scan the entire left side to find the max and the entire right side to find the max.
- Time: O(n^2). Space: O(1).

B. Dynamic Programming (Prefix/Suffix Arrays)
We can precompute the maximum height to the left and right for every index using two arrays: leftMax and rightMax.
    1. leftMax[i] stores the maximum height from index 0 to i.
    2. rightMax[i] stores the maximum height from index n-1 down to i.
    3. Iterate through the array once more to calculate trapped water using the formula above.
    Time Complexity: O(n) three passes
    Space Complexity" O(n) to store the two arrays.

C. Optimized: Two Pointers (The "Gold Standard")
We can optimize the space to O(1) by using two pointers, left and right.
    - We maintain leftMax and rightMax variables on the fly.
    - If height[left] < height[right], we know the bottleneck for left pointer is the leftMax (because there's a bar at right that is at least as tall as the current left side). We process the left side and move the pointer inward.
    - Otherwise, we process the right side.
    Time Complexity: O(n) one pass
    Space Complexit: O(1)

Dry Run:
Input Example 2: height = [4, 2, 0, 3, 2, 5]
1. Initialize: left = 0, right = 5, leftMax = 0, rightMax = 0, total = 0
2. Step 1: height[left] (4) vs height[right] (5). Left is smaller.
    - leftMax = max(0, 4) = 4.
    - Water added: 4 - 4 = 0.
    - left = 1
3. Step 2: height[left] (2) vs height[right] (5). Left is smaller.
    - leftMax = 4.
    - Water added: 4-2 = 2. total = 2.
    - left = 2
4. Step 3: height[left] (0) vs height[right] (5). Left is smaller.
    - leftMax = 4.
    - Water added = 4-0 = 4. total = 6.
    - left = 3
5. Step 4: height[left] (3) vs height[right] (5). Left is smaller.
    - leftMax = 4.
    - Water added = 4-3 = 1. total = 7.
    - left = 4
6. Step 5: height[left] (2) vs height[right] (5). Left is smaller.
    - leftMax = 4.
    - Water added = 4-2 = 2. total = 9.
    - left = 5
"""

from typing import List

class SolutionBF:
    def trap(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0

            # Search the left part for max bar size
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans


class SolutionO:
    # GFG: https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
    def maxWater(self, height):
        # code here
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                right -= 1

        return result

    # LC: https://leetcode.com/problems/trapping-rain-water/description/
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]
                right -= 1

        return result

solutionBF = SolutionBF()
solutionO = SolutionO()

print(f"Brute Force Solution: {solutionBF.trap([0,1,0,2,1,0,1,3,2,1,2,1])}")
print(f"GFG Solution: {solutionO.maxWater([3, 0, 1, 0, 4, 0, 2])}")
print(f"LC Solution: {solutionO.trap([0,1,0,2,1,0,1,3,2,1,2,1])}")