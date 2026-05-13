"""
Intuition: The matrix has a special property: elements increase
as you move right or down. This means the smallest element
is at mat[0][0] and the largest is at mat[n-1][n-1].
We can treat this as a search problem within a range of values.
Instead of searching thorugh indices, we search through
the value range [min, max]. If we pick a candidate number
X, we can quickly count how many elments in the matrix
are less than or equal to X. If that count is at least K, then
the Kth smallest element must be X or something smaller.

Approach: Binary Search on Value Range
We use Binary Search not on the array indices, but on the
possible values the answer could take.
    1. Initialize Range: Set low = mat[0][0] and high = mat[n-1][n-1].
    2. Binary Search Loop: While low < high:
        - Calculate mid = low + (high - low)//2.
        - Count elements <= mid: Use a pointer-based approach
        (starting from the bottom-left or top-right) to count
        how many elements in the matrix are less than or equal
        to mid in O(n) time.
        - Adjust Range:
            - If count < k: Our mid is too small, so low = mid + 1.
            - Else: Our mid might be the answer or is too large,
            so high = mid.
    3. Result: When the loop ends, low will be the Kth smallest element.

Helper Function: Counting in O(n)
Starting at the bottom-left (row=n-1, col=0):
    - If mat[row][col] <= mid: All elements above this in the
    same column are also <= mid. Add row + 1 to the count and
    move right (col++).
    - Else: The current element is too big, move up (row--).

Time Complexity:
    - Binary Search Range: The value range is Max-Min. Let R
    be the range. The binary search takes O(log(R)) iterations.
    - Counting Step: In each iteration, we traverse the matrix
    in O(n) time using the pointer method.
    - Total: O(n x log(R)).

Space Complexity:
    - O(1): We only use a few variables for pointers and
    counters. We do not use any extra data structures
    like heaps or auxiliary arrays.
"""


class Solution:
    # GFG: http://geeksforgeeks.org/problems/kth-element-in-matrix/1
    def kthSmallest(self, mat, k):
        # code here
        if not mat or not mat[0] or k > len(mat) * len(mat[0]):
            return -1

        n = len(mat)
        low = mat[0][0]
        high = mat[n - 1][n - 1]

        def countLessEqual(mid):
            count = 0
            c = 0
            r = n - 1

            while r >= 0 and c < n:
                if mat[r][c] <= mid:
                    count += r + 1
                    c += 1
                else:
                    r -= 1

            return count

        while low < high:
            mid = low + (high - low) // 2

            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

solutionGFG = Solution()
print(f"GFG Solution: {solutionGFG.kthSmallest([[16, 28, 60, 64],[22, 41, 63, 91], [27, 50, 87, 93],[36, 78, 87, 94]], 3)}")