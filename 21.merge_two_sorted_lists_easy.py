# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# 2 solutions:
# method 1. recursion
# method 2. iteration

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# method 1. recursion
# TC: O(m+n)
# SC: O(m+n)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Method 2: iteration
# TC: O(m+n)
# SC: O(1)

# Note: 注意 new_list 和 cur_list的运用
# cur_list像是new_list指向下一个的指针
# 把之前的保存好 （cur_list.next = l1， 留下l1的value），
# 然后继续往下走 （cur_list = cur_list.next）

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_list = ListNode('head')

        cur_list = new_list

        while l1 and l2:
            if l1.val <= l2.val:
                cur_list.next = l1
                l1 = l1.next
            elif l1.val>l2.val:
                cur_list.next = l2
                l2 = l2.next

            cur_list = cur_list.next

        cur_list.next = l1 or l2

        return new_list.next


