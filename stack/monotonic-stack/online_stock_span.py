"""
Intuition
The "span" of a stock price on day i is the number of consecutive
days (ending at i) where the price was less than or equal
to arr[i].
This is esentially asking: "find the nearest previous day
with a price strictly greater than today's price.
    - If such a day exists at index j, the span is i-j.
    - If no such day exists, it means today's price is the highest
    so far, so the span is i+1.
A Monotonic Decreasing Stack is perfect here because it allows us to "throw
away" smaller elements that are no longer relevnt, as the current higher
price will "shadow" them for all future days.

Approach: Monotonic Stack
Instead of comparing the current price against every single previous day,
we maintain a stack of indices whose prices are in strictly decreasing order.
    1. Initialize an empty stack to store indices and a res array of the same
    length as arr.
    2. Iterate through each price arr[i] at index i:
        - Pop Phase: While the stack is not empty and the price at the top of the
        stack is less than or equal to the current price arr[i], pop from the stack.
        Those popped days are now "covered" by the current day's higher price.
        - Calcuate Span:
            - If the stack is empty, today is the highest price seen so far. res[i] = i+1.
            - If stack is not empty, the top of the stack is the nearest index j where arr[j] > arr[i].
            res[i] = i - stack[-1].
        - Push Phase: Push the current index i onto the stack to serve as a potential "previous greater" for future days.

Time Complexity: O(n)
Athough there is a while loop inside a for loop, notice that each index
is pushed onto the stack exactly once and popped at most once. The total number of operations across the entire execution
is 2n (pushes and pops), which simplifies to O(n).

Space Complexity: O(n)
    - Auxiliary Space: In the worst-case scenario (prices in strictly decreasing order,
    e.g., [100, 80, 60, 40]), the stack will grow to size n.
    - Output Space: The res array also takes O(n) space.
"""


class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
    def calculateSpan(self, arr):
        # code here
        res = [1] * len(arr)
        stack = []  # Stores indices of prices in decreasing order

        for i, num in enumerate(arr):
            # Maintain monotonic decreasing property
            while stack and arr[stack[-1]] <= num:
                stack.pop()

            # If stack is empty, arr[i] is the maximum so far
            if not stack:
                res[i] = i + 1
            else:
                # Top of stack is the index of the nearest greater element
                res[i] = i - stack[-1]

            # Push current index
            stack.append(i)

        return res

"""
Intuition
The span for a day is the number of consecutive days ending today where the price was <= today's price.
If today's price is 85 and yesterday's was 75, we know the span for 85 must include 75 plus whatever 75 had already successfully "conquered" spans, we can "jump" over previous days instead of checking them one by one.

The Monotonic Stack Key
We use a decreasing monotonic stack.
    - If the new price is smaller than the top of the stack, its span is just 1.
    - If the new price is larger or equal to the top it "absorbs" the span of the previous price and we pop the stack. We repeat this until we find a price that is strictly greater than today's.

Approach
We store pairs in our stack: (price, span).
    1. Initialize an empty stack.
    2. For every next(price) call:
        - Set current_span = 1.
        - While the stack is not empty and the price at the top of the stack is <= the current price:
        - Pop the top element (prev_price, prev_span).
        - Add the prev_span to our current_span.
    3. Push the pair (price, current_span) onto the stack.
    4. Return current_span.

Time Complexity: O(1) (Amortized)
While a single call to next() might involve several pops from the stack (looking like O(N)), each price is pushed onto the stack exactly once and popped from the stack at most once across the entire lifetime of the StockSpanner object.
    - Total operations for N calls: O(N).
    - Average (amortized) time per call: O(1).

Space Complexity: O(N)
In the worst-case scenario (e.g., stock prices are in strictly decreasing order like [100, 80, 60, 40]), the stack will store every single price. Therefore, the space required is proportional to the number of calls made to next().
"""
class StockSpannerLC:
    # LC: https://leetcode.com/problems/online-stock-span/description/

    def __init__(self):
        # Stack stores pairs: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Pop elements from stack while the current price is greater
        # or equal to the price at the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

solutionGFG = SolutionGFG()
print(f"GFG Solution: {solutionGFG.calculateSpan([100, 80, 90, 120])}")
solutionLC = StockSpannerLC()
calls = [100, 80, 60, 70, 60, 75, 85]
results = []

for price in calls:
    results.append(solutionLC.next(price))

print(f"LC Solution: {results}")