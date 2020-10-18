# 445. Add Two Numbers II

# 思路：先把两个LinkedList分别放在stack里
# stack后进先出，所以就可以末尾相加了
# 注意：最后放回linkedList的时候，可以发生在同一个循环里

# TC：O(max(m,n))
# SC：O(m+n): 这是我们把链表内容放入栈中所用的空间。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        n1 = len(stack1)
        n2 = len(stack2)

        ans = None
        carry = 0
        # 注意： 这里多加了一个carry!=0
        while stack1 or stack2 or carry != 0:
            if stack1:
                s1 = stack1.pop()
            else:
                s1 = 0

            if stack2:
                s2 = stack2.pop()
            else:
                s2 = 0

            value = (s1 + s2 + carry) % 10
            carry = (s1 + s2 + carry) // 10

            # 注意，这一步很重要，注意顺序。
            cur_node = ListNode(value)
            cur_node.next = ans
            ans = cur_node

        return ans