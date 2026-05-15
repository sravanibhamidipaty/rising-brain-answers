class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_list(self):
        curr = self

        while curr:
            print(curr.data, end=" -> " if curr.next else "")
            curr = curr.next
        print()
"""
Time Complexity: O(n)
    - Since you only have the head pointer, you have to 
    traverse the entire list from the start to find the last
    node (where curr.next is None).
    - In the worst case, you visit every single one of the
    n nodes, making the operation linear.

Space Complexity: O(1)
    - You are performing an "in-place" modification of
    the existing structure.
    - While you are creating one new Node object, space
    complexity analysis for algorithms typically focuses on
    extra auxiliary space used relative to the input size.
    Since you aren't using any data structures that grow with
    n (like a list or a recursion stack), it remains constant.
"""


class Solution:
    def insertAtEnd(self, head, x):
        # code here
        if not head:
            return Node(x)

        curr = head
        while curr.next:
            curr = curr.next
        curr.next = Node(x)
        curr = curr.next
        curr.next = None
        return head

solution = Solution()
head = Node(1, Node(2, Node(3, Node(4))))
result = solution.insertAtEnd(head, 5)
print(f"GFG Solution: {result.print_list()}")