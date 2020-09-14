# 314. Binary Tree Vertical Order Traversal
#

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.


# method: 给坐标 （row, column）
# 和199 比较类似，199只给depth(row), 再加上一个column
# node.left, column-1
# node.right, column+1
# res 在199是一个 dic，key是depth（row），这里key改成[row, column]
# 最后结果就是找所有column一样的 row，按顺序排列

# two solutions: bfs, dfs

# Solution 1: dfs
# 利用stack，preOrder traversal，但是用一个list来记录both [node, [row, column]]
# 建立一个res dic, key = [row, column], value = node.val, 所以先进的就是最右边的node
# 最好一个min_column, max_column


import collections


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        min_column = 0
        max_column = 0
        stack = [[root, (0, 0)]]
        res = collections.defaultdict(list)

        while stack:
            node, (row, column) = stack.pop()
            if node:
                res[(row, column)].append(node.val) # 注意这里要用append，因为有的坐标是两个值
                max_column = max(max_column, column)
                min_column = min(min_column, column)
                # 这个地方要注意先right 再left，因为有的坐标会有两个值， append成了list，就得是左右的顺序
                if node.right:
                    stack.append([node.right, (row + 1, column + 1)])
                if node.left:
                    stack.append([node.left, (row + 1, column - 1)])


        # 开始遍历res，从左到右，从上到下建立list

        v_lists = []

        for c in range(min_column, max_column + 1):
            c_keys = []
            v_list = []
            for i in res.keys():
                if i[1] == c:
                    c_keys.append(i)
            c_keys.sort()
            for j in c_keys:
                v_list += res[j]
            v_lists.append(v_list)

        return v_lists


# Solution 2: BFS
# res = dict{}
# 利用一个queue (先进先出)，记录（node, (row, column))， list.pop(0)
# 每一次popleft，就是node的第一个，接着记录新的（node.left, (row+1, column-1)）,（node.right, (row+1, column+1)）
# update res[(row, column)] = node.val
## 最后结果就是找所有column一样的 row，按顺序排列

# TC: O(N)
# SC: O(N)

import collections


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = collections.defaultdict(list)
        max_column = 0
        min_column = 0
        queue = [[root, (0, 0)]]

        while queue:
            node, (row, column) = queue.pop(0)

            if node:
                res[(row, column)].append(node.val)
                max_column = max(max_column, column)
                min_column = min(min_column, column)
                # 先append左，再append右
                queue.append([node.left, (row + 1, column - 1)])
                queue.append([node.right, (row + 1, column + 1)])

        # 开始遍历res，从左到右，从上到下建立list

        print(min_column, max_column)
        v_lists = []
        print(res)
        for c in range(min_column, max_column + 1):
            c_keys = []
            v_list = []
            for i in res.keys():
                if i[1] == c:
                    c_keys.append(i)
            c_keys.sort()
            for j in c_keys:
                v_list += res[j]
            v_lists.append(v_list)

        return v_lists