# 429. N-ary Tree Level Order Traversal

# BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        res = collections.defaultdict(list)

        depth = 0
        queue = [(root, depth)]

        while queue:
            node, depth = queue.pop(0)
            if node:
                res[depth].append(node.val)
                for i in node.children:
                    if i:
                        queue.append((i, depth + 1))
        return [res[i] for i in res.keys()]

# DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


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
                c_node = node.children
                #注意要从后向前放在stack里
                c_node = c_node[::-1]
                for i in c_node:
                    stack.append((i, depth + 1))

        return [res[i] for i in res.keys()]