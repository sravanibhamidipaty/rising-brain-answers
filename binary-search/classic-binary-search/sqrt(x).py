class Solution:
    # LC: https://leetcode.com/problems/sqrtx/
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index

    # GFG: https://www.geeksforgeeks.org/problems/square-root/1
    def floorSqrt(self, n):
        # code here
        left = 0
        right = n
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == n:
                return mid
            if mid * mid < n:
                index = mid
                left = mid + 1
            else:
                right = mid - 1
        return index

solution = Solution()
print(f"GFG Solution: {solution.floorSqrt(4)}")
print(f"LC Solution: {solution.mySqrt(4)}")