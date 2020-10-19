# 这道题是高频题，所以是重点！
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

# 三种方法
# method 1. merge 2 lists，然后不停的merge下个list进入已经merge了的list
    # TC：O(kN), N is the sum of n of each list
    # SC: O(1), We can merge two sorted linked list in O(1) space.
# method 2. merge 2 lists, divide and merge: 每次merge两个list，然后再不停的往上merge
    # TC：O(NlogK)
    # SC: O(1), We can merge two sorted linked list in O(1) space.
# method 3：用最小堆 (heap)：建立最小堆，不停的把堆的头节点放到新的list里，然后push新的节点进堆，直到结束。
    # 利用了python的heapq.heapify() 建立最小堆， value就是最小堆的依据
    # heapq.heapify(list): 把list建立成最小堆
    # heaq.heappush(element): push一个element进最小堆
    # TC：O(NlogK), K number of elements in the list, 是heap的效率
    # SC: O(n), We can merge two sorted linked list in O(1) space.
# method 4: priority queue: 道理和heap差不多， 用value代表priorty，每一次update queue
    # 利用python的 from Queue import PriorityQueue，  q = PriorityQueue()
    # TC：O(NlogK)
    # SC: O(n), We can merge two sorted linked list in O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1
# merge list one by one
# TC: O(kN)
# SC: O()

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursive:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 1:
            return lists[0]
        if n == 0:
            # 注意这里是 ''
            return ListNode('')

        mlist = self.mergeTwoLists(lists[0], lists[1])

        for i in range(2, n):
            mlist = self.mergeTwoLists(mlist, lists[i])

        return mlist


# method 2. merge 2 lists, divide and merge: 每次merge两个list，然后再不停的往上merge
# Divide and merge

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursive:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 1:
            return lists[0]
        if n == 0:
            return ListNode('')

        new_list = []

        while len(lists) > 1:
            i = 0
            while i < n - 1:
                new_list.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                i += 2
            # 注意：这里要在最后一个是单个的时候来append一下
            if i == n - 1:
                new_list.append(lists[i])

            n = len(new_list)
            lists = new_list
            new_list = []

        return lists[0]

# Method 3
import heapq
from typing import List
# use priority queue的方法
# heapq package就是可以把建立和应用堆的
# heapq.heapify 把 h变成最小堆

import heapq
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # step 1: put head node value of each element in a list into a min heap
        k = len(lists)
        h = []
        for i in range(k):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        # ans, ans.next 就是最后要输出的 linkedlist， 通过cur_node来帮忙update
        ans = cur_node = ListNode()

        # 当h不为空的时候做如下操作
        while h:
            # idx 代表list的index
            # 1. pop 出堆里的最小值，变成一个node给cur.next,
            val, idx = heapq.heappop(h)
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

            # 2. 把下一个node放到堆里，自动找好了位置
            # #下一个node是刚才pop出去的那个点的同一个list的下一个node
            # 通过index来确认，index就是lists的index
            # 这种方式把 来取node的头节点 push到heap里，
            # 然后把这个list里的这个头节点去掉
            # 注意： lists[idx]实际上包括了刚才被pop出去的点，所以要等于next，node才是下一个点
            if lists[idx]:
                heapq.heappush(h, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return ans.next

lists = [[1,4,5],[1,3,4],[2,6]]
s = Solution()
s.mergeKLists(lists)



# Method 4：
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next