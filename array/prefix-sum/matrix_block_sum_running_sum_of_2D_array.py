from typing import List

"""
Time Complexity: The algorithm is divided into a one-time preprocessing
phase and an online querying phase.
- Preprocessing: We iterate through the N x M matrix once to compute
the prefix sums. Each cell involves a constant-time lookup
and three arithmetic operations giving us a strictly linear
O(N x M) time compexity.
- Querying: Because we precomputed the values, each submatrix sum query is
reduced to a constant-time lookup using the inclusion-exclusion principle.
This gives us O(1) per query.
- Overall: For Q queries, the total time is O(N x M + Q).

Space Complexity: We initialize a 2D array of size (N + 1) x (M + 1)
to store the cumulative sums. This results in auxiliary space
complexity of O(N x M)
Total Space: Including the input matrix and the output list
of size Q, the total space complexity is O(N x M + Q)
"""


class SolutionGFG:
    def prefixSum2D(self, mat, queries):
        # GFG: https://www.geeksforgeeks.org/problems/2d-submatrix-sum-queries/1
        # code here
        rows = len(mat)
        cols = len(mat[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )

        result = []

        for r1, c1, r2, c2 in queries:
            # Inclusion-Exclusion Principle
            current_sum = (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )
            result.append(current_sum)
        return result

"""
The goal of this problem is to find the sum of a 2k + 1 x 2k + 1 square around every single cell (i, j)

The challenge:
If we just use nested loops to calculate the sum for every cell, we'd be re-adding the same numbers over and over again. For a large matrix, that's way too slow.

How do we build the prefix sum?
To find the sum at P[i][j], you take the value from the original matrix and add the area above it and to its left. But wait--if you add the area to the left and the area above, you've added the top-left diagonal area twice! So you subtract it once to balance it out.

P[i][j] = mat[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

The Inclusion-Exclusion Trick

Now for the actual problem. You need the sum of a block centered at (i, j) with radius k. Let's define the boundaries of our target box:
r1, c1 (Top-Left): (i-k, j-k)
r2, c2 (Bottom-Right): (i+k, j+k)

To get the sum of just that box using our magic table P, we take the big rectange from (0, 0) to (r2, c2) and subtract the parts we don't need.

The formula looks like this:
Sum = P[r2][c2] - P[r1-1][c2] - P[r2][c1-1]+P[r1-1][c1-1]

Formula 1: Building the Prefix Sum Table
We want P[i][j] to represent the sum of all numbers in the rectangle from (0, 0) to (i, j).

P[i][j] = mat[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

- mat[i][j]: The value of the current cell itself.
- P[i-1][j]: The sum of the rectangle directly above our current cell.
- P[i][j-1]: The sum of the rectangle directly to the left of our current cell.
- The "-P[i-1][j-1]" part: When you add the "above" rectangle and the "left" rectangle, they both overlap at the top-left diagonal. You've added that diagonal section twice, so you subtract it once to fix the total.

Formula 2: Getting the Sum of a Specific block
Now, we need the sum of a specific window (from r1, c1 to r2, c2).

Sum = P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]

Think of this like a "cut-out" project:
1. P[r2][c2]: Start with the giant rectangle from the very beginning (0, 0) all the way to your bottom-right corner. This is too much data, so we start cutting.
2. - P[r1-1][c2]: Cut off the entire top section that sits above your desired box
3. - P[r2][c1-1]: Cut off the entire left section that sits to the left of your box
4. The + P[r1-1][c1-1] part: Look at the top left corner outside your box. Since you cut the top section AND left section, you actually cut that top-left corner out twice. You have a hole in your calculation. You add it back once to make the math perfect.

TC: O(m x n)
- Prefix Table Construction: We iterate through every cell of the m x n matrix exactly once to build the prefix table. Each cell takes O(1) constant time (just a few additions and subtractions).
- Result Caculation: We iterate through every cell of the matrix again to calculate the result. For each cell, we perform a O(1) lookup using our formula.
- Total: O(m x n) + O(m x n), which simiplifies to O(m x n).

SC: O(m x n)
- Prefix Table: We create an additional matrix of size (m + 1) x (n + 1) to store our cumulative sums.
- Output Matrix: The problem requires us to return a new m x n matrix.
- Total: Since both auxiliary structures scale linearly with the number of elements, the space complexity is O(m x n).
"""
class SolutionLC:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        # 1. Initialize a prefix sum table with extra padding (rows+1, cols+1)
        # This padding helps us avoid "out of bounds" checks for r-1 or c-1
        prefix = [[0]*(cols+1) for _ in range(rows+1)]

        # 2. Build the Prefix Sum Table
        # Formula: Current + Up + Left - DiagonalOverlap
        for r in range(rows):
            for c in range(cols):
                prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]

        # 3. Calculate the result for each cell
        result = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                # Determine the box boundaries (clamped within matrix limits)
                r1 = max(0, r-k)
                c1 = max(0, c-k)
                r2 = min(rows-1, r+k)
                c2 = min(cols-1, c+k)

                # Inclusion-Exclusion Formula using the prefix table
                # We use r2+1 because the prefix table is shifted by 1
                result[r][c] = (prefix[r2+1][c2+1]
                                - prefix[r1][c2+1]
                                - prefix[r2+1][c1]
                                + prefix[r1][c1])

        return result

solutionGFG = SolutionGFG()
solutionLC = SolutionLC()
print(f"GFG Solution: {solutionGFG.prefixSum2D([[1, 2, 3], [1, 1, 0], [4, 2, 2]], [[0, 0, 1, 1], [1, 0, 2, 2]])}")
print(f"LC Solution = {solutionLC.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)}")