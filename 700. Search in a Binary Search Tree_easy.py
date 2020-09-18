# 700. Search in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return null

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                if node.val > val:
                    stack.append(node.left)
                if node.val < val:
                    stack.append(node.right)
