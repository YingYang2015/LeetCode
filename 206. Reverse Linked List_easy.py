# 206. Reverse Linked List

# TC: O(N)
# SC: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        # stack: [1,2,3,4,5]
        # start from 5
        ans = cur_node = ListNode()

        while stack:
            cur_node.next = ListNode(stack.pop())
            cur_node = cur_node.next

        return ans.next

# TC: O(N)
# SC: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head
        curr = head
        ans = None
        while curr != None:
            tmp = curr.next
            curr.next = ans
            ans = curr
            curr = tmp

        return ans


# Recursion:
class Solution:
    def reverseList(self, C: ListNode, P = None) -> ListNode:
        if not C:
            return C
        t, C.next  = C.next, P
        return self.reverseList(t,C) if t else C