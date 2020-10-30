"""
Given a birnary tree, we want to find the minimum value of each level.

            5
          /   \
         2     1
        output: [5, 1]

             4
           /   \
          2      6
         / \    /
        3   1  5
        output: [4, 2, 1]

class Node:
    self.data = None: Int
    self.left = None: Node
    self.right = None: Node
"""


# level traverse


class Solution():
    def LevelMin(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        res = []
        depth = 0
        queue = [(root, depth)]

        while queue:
            node, depth = queue.pop(0)
            if len(res) < depth + 1:
                res[depth] = node.data

            if node:
                if node.data < res[depth]:
                    res[depth] = node.data

                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

        return res


"""
Given a 2D matrix of integers which contains zeros in some entries. 
If an element is 0, set its entire row and column to 0.
[[1, 2, 3]
 [0, 0, 6]
 [7, 8, 9]]

the output we want would be
[[0, 2, 3]
 [0, 0, 0]
 [0, 8, 9]]
"""


# traverse the matrix from top left to lowe right
# column number: n
# row # : m
# if x[i][j] == 0:
#    x[i] = [0]*n
#    for s in range(m):

class Solution:
    def MaxZero(self, x: List(List(int))) -> List(List(int)):
        if not x:
            return []
        m = len(x)
        n = len(x[0])

        dict = {}
        for i in range(m):
            if 0 in x[i]:
                dict[i] = True

        i = 0
        while i < m:
            if i in dict.keys():
                for j in range(n):
                    if x[i][j] == 0:
                        x[i] = [0] * n
                        for s in range(m):
                            x[s][j] = 0
            else:
                continue
            i += 1
        return x