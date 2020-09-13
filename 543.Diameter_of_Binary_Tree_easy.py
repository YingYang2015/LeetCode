# https://leetcode.com/problems/diameter-of-binary-tree/solution/

# Question:
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.


# Solution: Binary search tree, recursion, DFS
# 当站在一个node上
# L：depth: left child as a root (包括), maximum number of nodes
# R: depth: right child as a root (包括), maximum number of nodes

# 答案就应该是左边所有的nodes L, 加上右边所有的nodes R, + 1
# path 就是 answer -1

# TC: O(N), N is the number of nodes
# SC: O(N), the size of our implicit call stack during our depth-first search.
# 或者是 O(height), height 为二叉树的高度。由于递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，而递归的深度显然为二叉树的高度，并且每次递归调用的函数里又只用了常数个变量，所以所需空间复杂度为





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # ans is recording the maximum number of node we can connect

        self.ans = 1

        def depth(node):
            if not node:
                return 0

            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)

            return max(L, R) + 1

        depth(root)

        return self.ans - 1