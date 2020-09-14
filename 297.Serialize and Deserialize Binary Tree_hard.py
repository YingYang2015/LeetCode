# 297. Serialize and Deserialize Binary Tree
# 力扣：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution: DFS (比bfs更容易deserialize)
# serialize: 通过stack, DFS, 把他们放在一个list里
# 没有child的node，followed by 2 null
# deserialize： 用了recursion
# step 1：pop出来的第一个放到node，下面recursively给left和right， left和right都是node，如果没有了就是None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Solution: dfs stac
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node != None:
                res.append(node.val)
                # 注意这里如果没有了left，right，还是给了stack None
                stack.append(node.right) if node.right else stack.append(None)
                stack.append(node.left) if node.left else stack.append(None)
            else:
                # 注意：如果从stack里pop出来的node是None，放到res里，但是不进行其他操作了
                res.append(None)

        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []

        def TreeNodehelper(l):
            val = l.pop(0)
            if val == None:
                return None

            root = TreeNode(val)
            # 注意：这里两次都是l，原因是先left，left里面pop了0，所以到了right
            root.left = TreeNodehelper(l)
            root.right = TreeNodehelper(l)
            return root

        return TreeNodehelper(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))