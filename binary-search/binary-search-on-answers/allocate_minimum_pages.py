"""
Approach:
In the Allocate Minimum Pages problem, you are trying to find
the smallest maximum.
    - left (Lower Bound): This should be max(arr).
        - Why? You cannot allocate fewer pages than the
        largest single book in the array. If a book has
        90 pages, no student can have a "maximum" of only
        67 pages because someone has to take that 90-page
        book.
    - right (Upper Bound): sum(arr).
        - Why? This represents the case where only one
        student exists and must read every single book.

The canPlace(mid) Logic
Your helper function that needs to determine if you can
distribute the books such that no student gets more than
mid pages, using at most k students.

Logic for canPlace(mid):
    1. Initialize: students_count = 1 and current_pages_sum = 0.
    2. Iterate through each book in arr:
        - If current_pages_sum + book > mid:
            - This student can't take this book. Increment
            students_count.
            - Reset current_pages_sum to the current book.
        - Else:
            - Add the book's pages to current_pages_sum.
    3. Return students_count <= k

Time Complexity: O(N * log(D))
    - N is the number of elements in the array (the number of books).
    - D is the search space range, which is (sum(arr) - max(arr)).
    - We perform a binary search over the range D, and in each step,
      we iterate through the array of size N to verify if a
      distribution is possible.

Space Complexity: O(1)
    - The algorithm uses a constant amount of extra space for variables
      like low, high, mid, and students_count.
    - No additional data structures are created that scale with input size.
"""


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
    def findPages(self, arr, k):
        # code here
        if k > len(arr):
            return -1

        def canPlace(page):
            students_count = 1
            current_pages_sum = 0

            for book in arr:
                if current_pages_sum + book > mid:
                    students_count += 1
                    current_pages_sum = book
                else:
                    current_pages_sum += book

            return students_count <= k

        low = max(arr)
        high = sum(arr)
        res = -1

        while low <= high:
            mid = low + (high - low) // 2

            if canPlace(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
