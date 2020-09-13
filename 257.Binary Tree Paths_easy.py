# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.

# Solution 1: recursion (dfs)
# TC: O(N)
# SC: O(N)

# Solution 2: iteration (bfs)
# utilize stack, each element in the stack is a set (node, path to node (including the node val))
# step 1: have the stack start from root
# step 2: pop,
# if it is a leaf node: add the value to the path, the end, give path to paths
# if it is not a leaf node, goes to right, left seperately, path -> right, left
# TC: O(N)
# SC: O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # Solution 1: recursion (dfs)

        # this is all the paths together
        paths = []

        def construct_path(node, path):
            # path: means the existing path
            # everytime, will use the existing path, and the left (right) to construct new path
            # if the node is the leaf node, then just add this value to the path, the end, give this path to paths

            # path need to add the current node value
            if node is not None:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    # will be additional path
                    path += '->'
                    construct_path(node.left, path)
                    construct_path(node.right, path)

        # start with an empty path
        construct_path(root, '')

        return paths


# Solution 2: iteration, bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # Solution 2: iteration (bfs)
        # utilize stack, each element in the stack is a set (node, path to node (including the node val))
        # step 1: have the stack start from root
        # step 2: pop,
        # if it is a leaf node: add the value to the path, the end, give path to paths
        # if it is not a leaf node, goes to right, left seperately, path -> right, left

        # this is all the paths together
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if node.left is None and node.right is None:
                paths.append(path)
            if node.left:
                # 注意，不能在外面update path，必须直接写在括号里，要不然就把现在的path给update了
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths