# 257. Binary Tree Paths


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # Solution: recursion
        # start from root,
        # get_path
        # path = [left_path.append(root), right_path.append(root)]
        # left_path = get_path(root.left)
        # right_path = get_path(root.right)

        path = []

        def get_path(node):
            if not node:
                return []

            left_path = get_path(root.left)
            right_path = get_path(root.right)

            for i in left_path:
                i.append(node)
            for j in right_path:
                j.append(node)

            path = [left_path, right_path]

