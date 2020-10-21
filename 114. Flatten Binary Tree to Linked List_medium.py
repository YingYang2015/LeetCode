# 解题思路：
# one pass pre-order traversal, put traversal node into a new tree rightside, left = None

# TC: O(N)
# SC: O(N), new tree root (res)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        res = TreeNode(0)
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                # 注意：这里要直接等于node，不是node.val
                res.right = node
                res.left = None
                res = res.right
                stack.append(node.right)
                stack.append(node.left)

        return res


# SC是O(1) 的解法
# 中文力扣：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
# 设置一个cur，一个pre，一个next，cur是当前的node，pre，next是cur.left 刚开始是同一个node
# 如果cur.left不为空，就进行如下循环，一直到left空了

# 1.如果pre有right，就一直right到底，当前pre.right是空
    # 然后把cur_right放到pre.right里
# 2.然后把整个next放到cur.right, cur.left = None

# TC: O(N)
# SC: O(1)

class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
