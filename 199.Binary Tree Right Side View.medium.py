# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# 力扣： https://leetcode-cn.com/problems/binary-tree-right-side-view/solution/er-cha-shu-de-you-shi-tu-by-leetcode-solution/

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Method:
# 记录depth，然后找每一个depth的最右边的数字

# Solution 1: dfs
# 利用stack，类似preOrder traversal，但是用一个list来记录both [node, depth]
# preOrder traversal进stack的时候是先右后左，这里要先左后右，帮助先遍历右边所有的点
# 建立一个res dic, key = depth, value = node.val, 所以先进的就是最右边的node
# 然后再继续遍历左边的时候，如果keys里已经有这个depth了，就不update，说明最右边的点已经记录了
# 如果没有，就加入res dic

import collections


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = collections.defaultdict(list)

        depth = 0
        stack = [[root, depth]]

        while stack:
            # 此处和bfs不同， 是pop最有一个，bfs是pop最前面的一个
            node, depth = stack.pop()

            if node:
                # 此处和bfs不同，因为是by default最开始插入了右边的值
                if depth not in res.keys():
                    res[depth] = node.val
                if node.left is not None:
                    stack.append([node.left, depth + 1])
                if node.right is not None:
                    stack.append([node.right, depth + 1])

        res_list = [res[i] for i in res.keys()]
        return res_list


# Solution 2: bfs
# res = dict{}
# 利用一个queue (先进先出)，记录（node, depth)， list.pop(0)
# 每一次popleft，就是node的第一个，接着记录新的（node.left, depth+1）,（node.right, depth+1）
# update res[max_depth] = node.val
# 最后res就是每一个depth的最右边的数
# TC: O(N)
# SC: O(N)

import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = {}
        max_depth = 0
        depth = 0
        # queue = collections.deque([root, depth])
        queue = [[root, depth]]

        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            if node:
                res[max_depth] = node.val
                # 先append左，再append右
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])

        res_list = [res[i] for i in res.keys()]

        return res_list




