from typing import List

"""
Questions:
Can temperatures be empty?
Are temperatures valid numbers?
is temperatures array 0 indexed?

TC: O(N) where N is the number of elements in the temperatures array
SC: O(N) technically O(2N) one for stack and one for result array, but at max O(N) in the bigger bucket
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for current_index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_index = stack.pop()
                res[prev_index] = current_index - prev_index
            stack.append(current_index)
        return res