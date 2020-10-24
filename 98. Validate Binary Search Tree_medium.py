#  98. Validate Binary Search Tree

# 解题思路
# 1. DFS recursion
# maintain
# low: lowest value of the sub-tree,
# high: highest value of the sub-tree
# at each node, look at it's sub-tree, compare node.val with low and high, it should be in the middle, otherwise, return False
# 然后调用sub-tree
# 那么根据二叉搜索树的性质，在递归调用左子树时，
# for left node, 我们需要把上界 high 改为 root.val，即调用 helper(root.left, low, root.val)，因为左子树里所有节点的值均小于它的根节点的值。
# for right node: 我们需要把下界 low 改为 root.val，即调用 helper(root.right, root.val, high)
# TC: O(N)
# SC: O(N): since we keep up to the entire tree.


# 2. inorder traversal
# inorder traversal，是从左到右，从下到上，所以刚好满足了出来的排序必须是递增的。
# 两种方法，一种是：traversal完看是不是递增的
# 一种是traversal的时候直接判断，看是否>上面一个值，不大的话直接false
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2. inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre_val = [], float('-Inf')
        node = root

        while stack or node:
            while node:
                # 这里append当前的node
                stack.append(node)
                node = node.left

            node = stack.pop()
            cur_val = node.val

            if cur_val <= pre_val:
                return False

            node = node.right
            pre_val = cur_val

        return True

## 1. dfs recursion
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, low, high):
            if not node:
                return True
            val = node.val
            if val<=low or val >= high:
                return False

            if not helper(node.left, low, val):
                return False
            if not helper(node.right, val, high):
                return False
            return True

            # 注意：不能这么写！因为这样的话，到了一个empty node，helper function就停了， 所以必须按照上面那么写
            # helper(node.left, low, val)
            # helper(node.right, val, high)
            # return True

        return helper(root, float('-Inf'), float('Inf'))



