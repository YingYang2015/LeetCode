# 272. Closest Binary Search Tree Value II
# find the k closest node


# Solution:
# 先遍历了所有的点，求了diff
# 然后在对他们排队，找前k个


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        stack = [root]
        k_node = collections.defaultdict(list)

        while stack:
            node = stack.pop()
            if node:
                new_diff = node.val - target
                k_node[new_diff].append(node)

                stack.append(node.left)
                stack.append(node.right)

        l = list(k_node.keys())
        abs_l = list(set([abs(i) for i in l]))
        abs_l.sort()
        res = []
        for i in abs_l:
            if i != 0:
                tmp_node = k_node[i] + k_node[-i]
            else:
                tmp_node = k_node[i]
            for j in tmp_node:
                res.append(j.val)
        return res[0:k]
