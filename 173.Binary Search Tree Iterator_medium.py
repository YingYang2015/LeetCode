# 173. Binary Search Tree Iterator

# Solution: Inorder traversal
# Step 1: starting from root, goes to the left most node, put each node in stack in turn
# Step 2: pop the topnode, that is the smallest number
    # if this top node has a right child, stack right node and it's left most
# repeat, until the stack is empty

# TC: O(N)
# SC: O(h), h is the height of the tree, for stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]
        self.left_most(root)

    def left_most(self, node):
        if not node:
            return []

        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # print(self.stack)
        # topmost_node = self.stack.pop()

        res = []
        if self.stack:
            topmost_node = self.stack.pop()
            print('topmost_node', topmost_node)
            print(self.stack)
            if topmost_node.right:
                self.left_most(topmost_node.right)

            res = topmost_node.val
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        else:
            return False