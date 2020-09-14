# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# Solution: recursion
# standing on one node: total_sum = L_sum + R_sum + node.val
# define a a function of max_sum to calculate L and R sum
# 注意：1.要从-inf开始不能从0，因为有可能有负数
# 2. 要用 max(max_sum(node.left), 0)， 因为如果child的sum是负数的话，就不要了，给0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:


        self.ans = float('-inf')

        def max_sum(node):
            if not node:
                return 0

            L_sum = max(max_sum(node.left), 0)
            R_sum = max(max_sum(node.right), 0)

            self.ans = max(self.ans, L_sum + R_sum + node.val)

            return max(L_sum, R_sum) + node.val

        max_sum(root)

        return self.ans