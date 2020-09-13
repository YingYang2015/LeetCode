#
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

### 注意答案怎么建bfs的
# 主要问题： 我自己写的，BFS写的是对的， 但是前面graph建的不对

# 建graph
# 1. compare every 2 words
# 2. compare each letter in these 2 words
    # if letters are the same, move forward
    # if letters are different, record the node, move to next two words
    # if letters are always the same, and len(w1) > len(w2), 本身的order 有问题，return ""
# 注意：
    #1. 用 for else！ 意思是for完全执行了之后就执行else，如果for里有break，就跳出for
   # 非常好用！
   # 2. zip 遍历到len小的那个

# BFS：
# 要再研究一下！！
# TC: O(n^2 + M), n is the number of unique letters, M is the number of words in the list
# SC:

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Sort with BFS
        unique_l = list(in_degree.keys())
        path = []
        while len(unique_l) != 0:
            has_zerodegree = 0
            for j in unique_l:
                if in_degree[j] == 0:
                    in_degree[j] = -1
                    has_zerodegree = 1
                    break
            if has_zerodegree == 0:
                return ""

            path.append(j)
            unique_l.remove(j)

            for l in adj_list[j]:
                if l != adj_list[j]:
                    in_degree[l] -= 1

        path = path + unique_l
        return "".join(path)




# DFS
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Sort with DFS
        def dfs(i):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            for j in adj_list[i]:
                if dfs(j) == False:
                    return False

            visited[i] = 2
            path.append(i)
            return True

        unique_l = list(in_degree.keys())
        path = []
        visited = {}
        for i in unique_l:
            visited[i] = 0

        for i in unique_l:
            if dfs(i) == False:
                return ""
        res = path[::-1]

        return "".join(res)



# Complexity Analysis
#
# Let N be the total number of strings in the input list.
# Let C be the total length of all the words in the input list, added together.
# Let U be the total number of unique letters in the alien alphabet. While this is limited to 26 in the question description, we'll still look at how it would impact the complexity if it was not limited (as this could potentially be a follow-up question).

# Time complexity : O(C)
# There were three parts to the algorithm;
# 1. identifying all the relations,
# 2. putting them into an adjacency list
# 3. then converting it into a valid alphabet ordering.

# In the worst case, the first and second parts require checking every letter of every word
# (if the difference between two words was always in the last letter). This is O(C).
# For the third part, recall that a breadth-first search has a cost of O(V+E), where
# V is the number of vertices and E is the number of edges.
# Our algorithm has the same cost as BFS, as it too is visiting each edge and node once
# (a node is visited once all of its edges are visited, unlike the traditional BFS where it is visited once one edge is visited).
# Therefore, determining the cost of our algorithm requires determining how many nodes and edges there are in the graph.

# Nodes: We know that there is one vertex for each unique letter, i.e. O(U) vertices.
# Edges: Each edge in the graph was generated from comparing two adjacent words in the input list.
# There are # N-1 pairs of adjacent words, and only one edge can be generated from each pair.
# This might initially seem a bit surprising, so let's quickly look at an example. We'll use English words.