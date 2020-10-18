# 2. Add Two Numbers

# TC: O(max(m,n))
# SC: O(max(m,n)): 答案链表的长度


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = cur_node = ListNode()
        # ans = None
        carry = 0
        # 注意： 这里多加了一个carry!=0
        while l1 or l2 or carry != 0:
            if l1:
                s1 = l1.val
                l1 = l1.next
            else:
                s1 = 0

            if l2:
                s2 = l2.val
                l2 = l2.next
            else:
                s2 = 0

            value = (s1 + s2 + carry) % 10
            carry = (s1 + s2 + carry) // 10

            # 注意，这一步很重要，注意顺序。
            cur_node.next = ListNode(value)
            cur_node = cur_node.next

        return ans.next