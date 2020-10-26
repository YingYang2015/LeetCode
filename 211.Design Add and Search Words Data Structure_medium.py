# 211. Design Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Solution 1: 利用 length，每一次在length相同的words里面来找，每一个compare，
# 有满足的就return True，全不满足就return False
# TC：O(m*n): m is the length of the searched word,
# n is the number of words have the same length as the searched word
# SC：O(N)

#Solution 2: use trie
# Step 1: build a tri
# Step 2: search, use recursion, when meet '.', need to search for every child, therefore need a separate funtion for recursion

# Solution 2:
# 模版： https://blog.csdn.net/fuxuemingzhu/article/details/79390052?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160066895019725254049735%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=160066895019725254049735&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_blog_v1-1-79390052.pc_v2_rank_blog_v1&utm_term=211&spm=1018.2118.3001.4187
# TC: O(m)
# SC: O(1)
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current.children.keys():
                current.children[w] = Node()
            current = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        index = 0
        node = self.root
        return self.search_helper(word, index, node)



    def search_helper(word, index, node):
            if node == None:
                return False
            if index == len(word):
                return node.isword

            w = word[index]
            if w != '.':
                node = node.children.get(w)
                return node!= None and self.search_helper(word, index+1, node)
            if w == '.':
                for i in node.children.values():
                    if self.search_helper(word, index + 1, i):
                        return True
                return False




# Solution 1:
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        m = len(word)

        for dict_word in self.dict[m]:
            i = 0
            while i < m:
                if (word[i] == dict_word[i]) or (word[i] == '.'):
                    i += 1
                else:
                    break

            if i == m:
                return True

        return False