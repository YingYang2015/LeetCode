# 701. Insert into a Binary Search Tree
# insert a value to a BST

# 解题思路
# 遍历树，在一个node上比较node.val 和val的大小
# 如果val大，就相当于要插入右侧的 sub tree：node = node.right
# 如果val小，就相当于要插入左侧的 sub tree: node = node.left
# 接着比较node.val和val,直到
# node.val < val and node.right is empty, 插入
# or node.val > val and node.left is empty, 插入



# Solution 1: Iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # TODO：这里要要把root给node
        node = root
        if not root:
            return TreeNode(val)

        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    # TODO：这里要return root
                    return root
                else:
                    node = node.right

            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return root


# Solution 2: recursion
# TC: O(H)
# SC: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)

        return root

