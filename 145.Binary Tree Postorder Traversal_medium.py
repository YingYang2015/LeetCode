# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Bottom to top
# left to right

# Solution 1: Recursion
# TC: O(N)s
# SC: O(N)

# Solution 2: iteration, bfs
# 实际上是前序遍历，进stack的order是 根-左-右，然后return res[::-1]
# TC: O(N)
# SC: O(N)

# Solution 3:
# Step 1：先把所有的node都进堆
    # case 1： 怎么进堆：右，根，左，当左有child的时候，继续对这个左node先进右，然后进自己，然后再进他的左，一直进行下去
    # case 2： 但是这会让如果右node有child就第一次进不去
# Step 2：出堆，然后处理右侧还没进堆的情况，case 2




# Solution 1: Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) +[root.val]

# Solution 2
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                # 注意这边要先左再右
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        return res[::-1]


# Solution 3:
# Step 1：先把所有的node都进堆
    # case 1： 怎么进堆：右，根，左，当左有child的时候，继续对这个左node先进右，然后进自己，然后再进他的左，一直进行下去
    # case 2： 但是这会让如果右node有child就第一次进不去
# Step 2：出堆，然后处理右侧还没进堆的情况，case 2


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None

        return output