# 785. Is Graph Bipartite?
# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# 解题思路：
# 站在每一个点上，给他的两个neigbour染成不同的颜色
# 给第一个node： red
# 建立一个hash table：记录已经被染色了的node 的颜色
# 还需要一个visited list, 记录已经visited的，而且染过it's neighbor的 node
# 遍历graph的node(index), 如果还没有染色，就染色，如果染色了，看颜色是否一致，一致就继续，不一致就False

# 1. 遍历的话可以通过bfs （use stack),
# 问题是如果是Bipartite， 怎么出来 (visited)
# 但是这个不能用通过whie stack来，(tree可以，graph不可以)
# 因为有可能这个grpah里面有两个独立的graph，这样的话查了一个之后就跳不到另外一个去
# 所以需要通过遍历每一个node for i in range(n)
# 2. 也可以通过dfs

# TC: O(N+M): N: nodes, M: edges
# SC: O(N): color_dict 和visited

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        # visited: it means it's neighbor nodes are colored
        visited = [0] * n
        # red: 1, green: -1
        color_dict = {}
        color_dict[0] = 1
        # node
        # stack = [0]
        stack = []

        for i in range(n):
            if visited[i] == 0:
                stack.append(i)

            while stack:
                node = stack.pop()
                if node not in color_dict.keys():
                    color_dict[node] = 1
                if not graph[node]:
                    continue
                for j in graph[node]:
                    if j not in color_dict.keys():
                        color_dict[j] = -color_dict[node]
                    elif color_dict[j] == color_dict[node]:
                        return False
                    if visited[j] == 0:
                        stack.append(j)

                visited[node] = 1

        return True

# DFS快一些：

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        创建flags颜色标记数组，颜色0表示未被访问时节点的颜色，1和-1分别是访问后需要染的颜色
        所谓二分图其实可以换个思路，即一条边上的两个点一定分属两个集合，因此颜色必定不相同
        '''
        n = len(graph)
        visited = [0] * n

        def dfs(start, color):
            # dfs true means 下面都成立

            # 当前的node是没有被访问过的，所以先给1
            visited[start] = color

            for i in graph[start]:
                # neighbor 的color等于自己的color
                # 或者neighbor没有被染色呢，但是他不是和node的相反color
                if visited[i] == color or (visited[i] == 0 and not dfs(i, -1 * color)):
                    return False

            return True

        for i in range(len(graph)):
            # 如果没有被visit，就给color 1， 所以是dfs(i,1)
            if visited[i] == 0 and not dfs(i, 1):
                return False

        return True