# 1522. Diameter of N-Ary Tree
# https://leetcode.com/problems/diameter-of-n-ary-tree/
# Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.
# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.
# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)


# Solution: N-Ary tree, recursion, DFS
# 当站在一个node上
# 每一个child (i in node.childen)：depth: child as a root (包括), maximum number of nodes

# 答案就是 top 2 depth + 1
# path 就是 answer -1

# TC: O(N), N is the number of nodes
# SC: O(N), the size of our implicit call stack during our depth-first search.
# 或者是 O(height), height 为二叉树的高度。由于递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，而递归的深度显然为二叉树的高度，并且每次递归调用的函数里又只用了常数个变量，所以所需空间复杂度为





"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:

        self.ans = 1

        def depth(root):
            if not root:
                return 0

            max_depth = 0
            for i in root.children:
                branch_depth = depth(i)
                self.ans = max(self.ans, branch_depth + max_depth + 1)
                max_depth = max(max_depth, branch_depth)

            return max_depth + 1

        depth(root)
        return self.ans - 1