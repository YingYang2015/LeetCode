# 230. Kth Smallest Element in a BST
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# 解题思路： in order traversal，贴到k的时候返回

# TC: O(N)
# SC: O(k)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        l = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            l.append(node.val)
            if len(l) == k:
                return node.val
            node = node.right


