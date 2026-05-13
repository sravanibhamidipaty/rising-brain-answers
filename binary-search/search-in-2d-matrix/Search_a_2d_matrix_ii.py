from typing import List

"""
Intuition: The Sorted Search Space
The key is to find a starting point that allows us to make a binary decision.
    - If we start at the top-left, moving right or down both increase the value. We can't prune the search space.
    - If we start at the top-right, moving left decreases the value, while moving down increases it.

This transforms the 2D grid into a conceptual Binary Search Tree, where the top-right corner is the root. The "left child" is the element to the left, and the "right child" is the element below.

Approach: Staircase Search
We initialize our pointers at the top-right corner:
row = 0, col = n - 1.
    - Comparison: Compre the current element matrix[row][col] with the target.
    - Case 1 (Found): If current == target, return true.
    - Case 2 (Too Big): If current > target, then every element below current in that column is also too big (since columns are sorted). We can safely eliminate the entire column by moving col -= 1.
    - Case 3 (Too Small): If current < target, then every element to the left of current in that row is also too small (since rows are sorted). We can safely eliminate the entire row by moving row += 1.
Termination: Repeat until the target is found or the pointers move out of bounds.

Complexity Analysis:
Time Complexity: O(m + n) where m is the number of rows and n is the number of columns.
Space Complexity: O(1)
"""
class SolutionLC:
    # LC: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols-1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
        return False

"""
Time Complexity: O(log(M x N))
    - Performing a standard binary search over M x N total
    elements, the search space halves with each iteration.
    - This can also be expressed as O(log M + log N) based
    on logarithmic properties.

Space Complexity: O(1)
    - The algorithm only requires a constant amount of extra
    space for variables like left, right, mid, rows, and cols.
    - You are performing the search in-place by mapping the
    1D index back to 2D coordinates using:
        - row = mid // cols
        - cols = mid % cols
"""
class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1
    def searchMatrix(self, mat, x):
        # code here
        rows = len(mat)
        cols = len(mat[0])

        if not rows or not cols:
            return False

        left = 0
        right = rows*cols-1

        while left <= right:
            mid = left + (right-left)//2

            if mat[mid//cols][mid%cols] == x:
                return True
            elif mat[mid//cols][mid%cols] < x:
                left = mid + 1
            else:
                right = mid - 1
        return False

solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)}")
print(f"GFG Solution: {solutionGFG.searchMatrix([[1, 5, 9], [14, 20, 21], [30, 34, 43]], 14)}")