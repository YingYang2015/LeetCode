# 141. Linked List Cycle
# 快慢指针

# TC: O(N)
# SC: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False



# 第二种方法
# TC: O(N)
# SC: O(N)
# 注意：这里要用 head，不能用head.val，
# 因为是一个循环的linkedList，两个node的值可能相同，但是不代表是一个循环
# 只有head后面完全一样，才证明是循环


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        current_set = []

        while head:
            # 注意：这里要用 head，不能用head.val
            if head in current_set:
                return True
            current_set.append(head)

            head = head.next

        return False