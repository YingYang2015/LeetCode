# 94. Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.
# 结果是从左到右

# Solution 1: recursion
# 递归方法比较简单，直接按照左子树->该节点->右子树的顺序遍历即可。
# TC: O(N)
# SC: O(N)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return []

        if root.left is not None:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right is not None:
            res.extend(self.inorderTraversal(root.right))

        return res


# Solution 2: iteration,
# TC: O(N)
# SC: O(N)


# 迭代解法需要用到栈，这个方法确实比递归难得多了。
# 我们先把节点所有的左节点放入栈中，然后开始出栈，每次出栈都把栈中的元素放入到结果中，并且把这个结果的右孩子放入栈中。
# 因此，这里的遍历顺序先沿着最左方向到达最左下角的孩子，然后每次弹出来一个节点，
# # 把该节点的值放入结果中，并开始处理该节点的右子树


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        answer = []
        node = root

        while stack or node:
            # 一直向下走到最左边的node，依次放到堆里
            while node:
                stack.append(node)
                node = node.left

            # pop出一个来，给result，如果右边还有child，就接着去右边，在右边继续往它自己的左边走
            node = stack.pop()
            answer.append(node.val)
            node = node.right

        return answer
