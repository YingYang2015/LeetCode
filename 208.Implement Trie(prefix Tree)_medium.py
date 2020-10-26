# Implement a trie with insert, search, and startsWith methods.

# 模版： https://blog.csdn.net/fuxuemingzhu/article/details/79388432
# 每个节点的子孩子都是一个字典，根据字典查找下一个位置的节点，就像字典一样。
#
# 同时用isword保存当前是不是一个词（也可能是路径中的点）。

# TC: O(m): In each step of the algorithm we search for the next key character. In the worst case the algorithm performs
# m operations.
# SC: O(m)
class Node():
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False

class Trie:

    def __init__(self):
        # 初始化trie, the first node is not a word
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for w in word:
            if w not in current.children.keys():
                current.children[w] = Node()
            current = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)