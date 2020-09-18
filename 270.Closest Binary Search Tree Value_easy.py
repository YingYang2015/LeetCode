#  Closest Binary Search Tree Value

#
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# TC: O(H): since here one goes from root down to a leaf.
# SC: O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        stack = [root]
        min_node = root
        diff = float('Inf')

        while stack:
            node = stack.pop()
            if node:
                if abs(node.val - target) < diff:
                    min_node = node

                diff = min(diff, abs(node.val - target))

                if node.val - target > 0:
                    stack.append(node.left)
                if node.val - target < 0:
                    stack.append(node.right)

        return min_node.val

