# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(N), n is the number of node
# SC: O(H), h is the height of the tree
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        stack = [root]
        ans = 0
        # root.val in the middle, l_node = node.left, right_node = node.right
        # root.val >L, go to node.left
        # root.val < R, go to node.right

        while stack:
            node = stack.pop()
            if node:
                if node.val >= L and node.val <= R:
                    ans += node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans



class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans