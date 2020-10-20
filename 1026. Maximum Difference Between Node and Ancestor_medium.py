# 1026. Maximum Difference Between Node and Ancestor
# Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

# (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

# 解题思路
# 创建一个当前最大值和当前最小值
# 每遍历到一个点的时候，就calculate当前node.val和最大最小值的差
# 这个差的绝对值就会是最大的absolute number
# 需要利用一个helper function来recursively do it

# TC: O(N)
# SC: O(N): since we need stacks to do recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:


        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min

            cur_max = max(node.val, cur_max)
            cur_min = min(node.val, cur_min)

            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)

            return max(left, right)

        return helper(root, root.val, root.val)
