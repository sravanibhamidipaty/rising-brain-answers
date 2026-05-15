"""
Time Complexity: O(n)
In the worst case, the key you are looking for is at the
very last node of the list or is not present at all. In this
scenario, the while head: loop must visit every single node
exactly once. Therefore, the time taken grows linearly with
the number of nodes n.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space. It
only maintains a pointer (or reference) to the current node
as it traverses the list. It does not use any additional
data structures or recursion (which would add to the call stack),
so the space usage remains constant regardless of the list size.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    # GFG: https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
    def searchKey(self, head, key):
        # Code here

        while head:
            if head.data == key:
                return True
            head = head.next
        return False

solution = Solution()
head = Node(1, Node(2, Node(3, Node(4, None))))
print(f"GFG Solution: {solution.searchKey(head, 3)}")