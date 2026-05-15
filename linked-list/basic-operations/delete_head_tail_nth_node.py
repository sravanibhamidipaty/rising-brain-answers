from typing import Optional, List

"""
Intuition
To delete a node in a singly linked list, you need to reach
the node immediately preceding the one you want to delete.
Once you are at the (x-1)th node, you can simply "skip"
the xth node by pointing the current node's next pointer to
curr.next.next. A special case exists if x = 1: there is
no "preceding" node, so you must move the head pointer to
the second node.

2. Approach
    1. Handle the Head: If x == 1, the new head of the list
    becomes head.next. Return this immediately.
    2. Traverse: Use a loop to move a pointer curr from the head
    to the (x-1)th position. Since it is 1-based indexing, you
    need to jump x-2 times from the head to land on the node
    right before the target.
    3. Relink: Set xurr.next = curr.next.next. Python's garbage
    collection will handle with the memory for the unlinked node.
    4. Return: Return the original head.

Complexity Analysis
Time Complexity: O(n)
    - In the worst case (deleting the last node), we must
    traverse the entire list of n nodes. Each node is visited
    at most once.

Space Complexity: O(1)
    - We are only using a single pointer (curr) and an integer
    (count) regardless of the size of the linked list. No
    additional data structures are created.
"""

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

class SolutionGFG:
    # GFG: https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1
    def deleteNode(self, head, x):
        # code here
        # Case 1: Delete the head node
        if x == 1:
            return head.next

        curr = head
        # Move to the (x-1)th node
        # We use counter to track our position
        count = 1
        while count < x - 1 and curr is not None:
            curr = curr.next
            count += 1

        # Case 2: Delete the x-th node by skipping it
        if curr is not None and curr.next is not None:
            curr.next = curr.next.next

        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        curr = self

        while curr:
            print(curr.val, end= " -> " if curr.next else "")
            curr = curr.next
        print()

"""
Questions:
- Can head be null? Yes
- Can n be more than the number of nodes, if so what do I return? None

Intuition:
Convert the linked list into an array and then remove the element nth element and convert the array
back to a linked list. TC: O(m) where m is the number of nodes in the linked list SC: O(m) where m is the number of nodes in the linked list.

Approach:
Two pointers
Slow pointer and Fast pointer.

Slow pointer and fast pointer point to head
Have fast pointer move n places ahead.
1 -> 2 -> 3 -> 4 -> 5
sf

1 -> 2 -> 3 -> 4 -> 5
s         f

Move both slow and fast.
slow to the next pointer
and fast to the next next
1 -> 2 -> 3 -> 4 -> 5
     s         f

1 -> 2 -> 3 -> 4 -> 5
          s         f

slow.next = slow.next.next
At 3 point to 5
Return head

TC: O(m) where m is the number of nodes in the linked list
SC: O(1)
"""


class SolutionLC:
    # LC: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # 1. Create a dummy node that points to the head
        dummy = ListNode(next=head)
        slow = fast = dummy

        # 2. Move fast pointer n steps ahead
        # Starting from dummy, fast will now be at the
        # n-th node
        for _ in range(n):
            fast = fast.next

            # 3. Move both until fast reaches the last node
        # slow will stop exactly one node BEFORE the target
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 4. Skip the target node
        slow.next = slow.next.next

        # 5. Return dummy.next (the new head)
        return dummy.next

solutionGFG = SolutionGFG()
head = Node(1, Node(2, Node(3, Node(4))))
solutionGFG.deleteNode(head, 2)
head.print_list()

solutionLC = SolutionLC()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = solutionLC.removeNthFromEnd(head, 3)
result.print_list()