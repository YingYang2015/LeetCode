
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        # 0 = Unknown, 1 = visiting, 2 = visited
        print(graph)
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            print('start i', i)
            if not self.dfs(graph, visited, i, path):
                return []
        return path[::-1]

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        print(i, 'visited[i]', visited[i])
        print(i, 'graph[i]', graph[i])
        for j in graph[i]:
            print(j, self.dfs(graph, visited, j, path))
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2

        print(i, 'visited[i]', visited[i])
        path.append(i)
        print('\n')
        return True

s = Solution()
numCourses = 5
prerequisites = [[2,1], [4,2],[3,2], [3,4], [1,0]]
print(s.findOrder(numCourses, prerequisites))