# 133. Clone Graph

# 解题思路： BFS
# 从原来的node里，每一次clone那个node的value， 放到一个lookup里
# lookup是一个dict， key：原始的node，vaulue：就是要新组建的，clone过来的
# 通过queue来遍历 原来的graph上的node
# 如果这个node （tmp）不在lookup里，就放进lookup里，开始建立Clone，从value开始建立
# 然后lookup[tmp]的neighbor就是tmp的neighbor在lookup里的样子lookup[n]
# 通过clone = lookup[node], 来update，最后return哪个都可以

# 需要一个lookup的原因是，为了产生每一个node，记录在value里

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        lookup = {}

        if not node:
            return node

        clone = Node(node.val, [])
        lookup[node] = clone
        queue = [node]

        while queue:
            tmp = queue.pop(0)

            for n in tmp.neighbors:
                if n not in lookup:
                    lookup[n] = Node(n.val, [])
                    queue.append(n)
                lookup[tmp].neighbors.append(lookup[n])

        return clone

