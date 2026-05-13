from typing import List

"""
Time Complexity: O(log(m x n)). The algorithm performs a binary search over a range of size m x n. Since binary search halves the search space in each iteration, it takes logarithmic time relative to the total number of elements.

Space Complexity: O(1). Only using a constant amount of extra space for variables like left, right, mid, rows, and cols. No additional data structures are created that scale with the input size.
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/search-a-2d-matrix/description/
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# User function Template for python3
"""
Intuition
The key is to find a starting point where you can make a binary
decision--a point where one direction strictly increases the
values and the other strictly decreases them.
    - The Problem with (0, 0): If you start at the top-left, both
    right and down increase the values. You don't know which way to go.
    - The "Pivots": The top-right (0, m-1) and bottom-left (n-1, 0)
    are perfect. From the top-right:
        - If the current element is greater than x, x must be to the
        left (entire column is ruled out).
        - If the current element is smaller than x, x must be to the 
        below (entire row is ruled out).

Approach (Staircase Search)
We will start at the top-right corner and treat the matrix like a
pruned search tree:
    1. Initialize row = 0 and col = m-1
    2. While row is within the total rows and col >= 0:
        - If mat[row][col] == x, return true.
        - If mat[row][col] > x: Move left (col -= 1) because all
        elements below this point in the current column are even larger
        - If mat[row][col] < x: Move down (row += 1) because all
        elements to the left in this row are even smaller.
    3. If the loop finishes without a match, return false.

Complexity Analysis
Time Complexity: O(n + m): In the worst case, you start at the top-right
and end at the bottom-left. You perform at most n downward moves and
m leftward moves. This is significantly better than O(n x m) or
even O(n log m).

Space Complexity: O(1): We only use a few variables to track the
current row and column indices; no extra data structures are required.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1
    def matSearch(self, mat, x):
        # Complete this function
        if not mat or not mat[0]:
            return False

        rows = len(mat)
        cols = len(mat[0])
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                row += 1
            elif mat[row][col] > x:
                col -= 1

        return False


solutionLC = SolutionLC()
solutionGFG = SolutionGFG()
print(f"LC Solution: {solutionLC.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)}")
print(f"GFG Solution: {solutionGFG.matSearch([[3, 30, 38],[20, 52, 54],[35, 60, 69]], 62)}")