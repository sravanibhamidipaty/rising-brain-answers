"""
Time Complexity: O(n)
    - You must iterate through the array exactly once
    to visit every element.

Space Complexity: O(n)
    - While you are technically correct that the process
    requires O(n) space, a top-tier candidate should clarify
    the context:
        - Total Space Complexity (O(n)): This includes the
        space required to store the output. Since the problem
        explicitly asks you to "construct a linked list,"
        the n nodes are a requirement of the output.
        - Auxiliary Space (O(1)): This refers to the extra
        space used by your algorithm excluding the input and
        output. In your current implementation, you only use
        a few pointers (head, curr), whic is constant space.
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
    # GFG: https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1
    def arrayToList(self, arr):
        # code here
        if not arr:
            return None

        if len(arr) == 1:
            return Node(arr[0])

        head = Node(0)
        curr = head

        for num in arr:
            curr.next = Node(num)
            curr = curr.next

        return head.next

solutionGFG = SolutionGFG()
print(f"GFG Solution:", end= " ")
solutionGFG.arrayToList([1, 2, 3, 4, 5]).print_list()


"""
Intuition
Think of a Linked List like a scavenger hunt. You only know where the first clue is. To find the i-th clue, you must follow the trail one by one. By adding a "dummy" node at the very beginning, we ensure the "first" real node always has a "previous" node, which makes adding/deleting at the head identical to adding/deleting anywhere else.

Approach (Singly Linked List)
    - Node Class: A simple object with val and next.
    - Sentinel Node: Initialize self.head as a dummy node. This avoids if index == 0 logic everywhere.
    - Size Tracking: Maintain a self.size variable to instantly validate indices.
    - Traversal: Create a helper function or loop that moves or curr pointer index times to reach the desired position.

Complexity Analysis
get
    - Time Complexity: O(k)
    - Space Complexity: O(1)
    - Reasoning: Where k is the index; must traverse nodes.

addAtHead
    - Time Complexity: O(1)
    - Space Complexity: O(1)
    - Reasoning: Insertion is immediate (using addAtIndex(0))

addAtTail
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    - Reasoning: Must traverse the entire list to find the end.

addAtIndex
    - O(k)
    - O(1)
    - Reasoning: Must traverse to the k-th node.

deleteAtIndex
    - O(k)
    - O(1)
    - Reasoning: Must traverse to the node before the k-th node.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedListLC:
    # LC: https://leetcode.com/problems/design-linked-list/
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # Sentinel/Dummy node

    def print_list(self):
        curr = self.head.next

        while curr:
            print(curr.val, end= " -> " if curr.next else "")
            curr = curr.next
        print()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # Move index + 1 steps because we start at the sentinel
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        self.size += 1
        prev = self.head
        for _ in range(index):
            prev = prev.next

        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next

myLinkedListLC = MyLinkedListLC()
myLinkedListLC.addAtHead(1)
myLinkedListLC.addAtTail(3)
myLinkedListLC.addAtIndex(1, 2)
print(f"LC Solution: {myLinkedListLC.get(1)}")
myLinkedListLC.deleteAtIndex(1)
print(f"LC Solution: {myLinkedListLC.get(1)}")
print(f"LC Solution:", end=" ")
myLinkedListLC.print_list()