# 328. Odd Even Linked List
#  题目：一个linkedlist，变成新的linkedlist，display odd items first then even items


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 解题思路：

# 遍历LinkedList，用一个index来计数，如果是odd就给odd_list, even就给even list
# 需要注意的是
# 1. 需要给both even_list和odd_list 一个current_node, update current_node的时候来update even_list 和odd_list.
# 2. 最后给even_list.next is None, otherwise后面会带着oddlist
# 3. update cur_odd_node, 来把even_list连上

# TC: O(N)
# SC: O(1): it is still O(1) space because those 2 new list nodes do not grow relative to the size of the input. You only have 2 list nodes whether the initial linked list has 5 nodes or 5 million.

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        i = 1
        even_list = cur_even_node = ListNode()
        odd_list = cur_odd_node = ListNode()

        while head:
            if head:
                if i % 2 == 1:
                    cur_odd_node.next = head
                    cur_odd_node = cur_odd_node.next
                else:
                    cur_even_node.next = head
                    cur_even_node = cur_even_node.next

                i += 1
                head = head.next
        # 注意：给even_list.next is None, otherwise后面会带着oddlist
        cur_even_node.next = None
        # 注意：update cur_odd_node, 来把even_list连上
        cur_odd_node.next = even_list.next

        return odd_list.next
