# Solution 1: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = collections.defaultdict(list)

        depth = 0
        queue = [(root, depth)]

        while queue:
            node, depth = queue.pop(0)
            if node:
                res[depth].append(node.val)
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
        res_list = [res[i] for i in res.keys()]
        return res_list[::-1]

# Solution 2: DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = collections.defaultdict(list)
        depth = 0
        stack = [(root, depth)]
        while stack:
            node, depth = stack.pop()
            if node:
                res[depth].append(node.val)
                if node.right:
                    stack.append((node.right, depth + 1))
                if node.left:
                    stack.append((node.left, depth + 1))

        res_list = [res[i] for i in res.keys()]
        return res_list[::-1]