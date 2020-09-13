# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Given a binary tree, return the preorder traversal of its nodes' values.

# preorder: top -> bottom, left -> right


# Solution 1: recursion
# TC: O(N)
# SC: O(N)
# Solution 2: iteration
 # use stack, start from the top, 1. put the node into a stack
 # 2. pop, if it is a leaf, append to the list,
 # if it is not a leaf, append value to the list, put left and right to stack,
 # 3. continue until nothing in stack
 # using stack to ensure to go over all the nodes
# TC: O(N)
# SC: O(N)

# Solution 1: recursion
# TC: O(N)
# SC: O(N)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return []
        res.append(root.val)
        if root.left is not None:
            res.extend(self.preorderTraversal(root.left))
        if root.right is not None:
            res.extend(self.preorderTraversal(root.right))
        return res


# Solution 2: iteration
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                # 这边一定要先right，再left, 因为pop的时候是先出来left
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)

        return res


