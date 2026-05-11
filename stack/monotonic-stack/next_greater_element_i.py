from typing import List

"""
TC: O(n+m)
    - Pre-processing num2: You iterate through nums2 once. Each element is pushed onto and popped from the stack exactly once, leading to O(m).
    - Mapping nums1: You iterate through nums1 once and perform an O(1) dictionary lookup for each element leading to O(n).
    - Total O(n + m)

SC: O(m)
    - Hash Map (next_greater): In the worst case (e.g., a strictly decreasing array), you might store nearly all m elements.
    - Stack: In the worst case, the stack could also hold m elements.
    - Total O(m) to store the relationships between elements in nums2.
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        res = [-1] * len(nums1)
        stack = []

        for i, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                next_greater[nums2[stack[-1]]] = num
                stack.pop()
            stack.append(i)

        for i, num in enumerate(nums1):
            if num in next_greater:
                res[i] = next_greater[num]

        return res

"""
TC: O(n)
    - Each index of the array is pushed onto the stack exactly once.
    - Each index is popped from the stack at most once (when its
    "next greater" element is found).
    - Since both push and pop operations are O(1), the total time
    spent managing the stack across the entire loop is O(n).

SC: O(n)
    - Result Array: We maintain a res array of size n to store the output.
    - Stack: In the worst-case scenario (e.g., a sorted array in descending
    order like [5, 4, 3, 2, 1]), the stack will store all n indices before
    any are popped.
"""

class SolutionLC:
    # LC: https://leetcode.com/problems/next-greater-element-i/description/
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        res = [-1] * len(nums1)
        stack = []

        for i, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                next_greater[nums2[stack[-1]]] = num
                stack.pop()
            stack.append(i)

        for i, num in enumerate(nums1):
            if num in next_greater:
                res[i] = next_greater[num]

        return res


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
    def nextLargerElement(self, arr):
        # code here
        res = [-1] * len(arr)
        stack = []

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)

        return res

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.nextGreaterElement([4,1,2], [1, 3, 4, 2])}")
print(f"GFG Solution: {solutionGFG.nextLargerElement( [1, 3, 2, 4])}")