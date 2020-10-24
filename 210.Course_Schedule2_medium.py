# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# and return the path

# Solution 1: BFS
# Step 1: create a graph with edge nodes, using prerequisites
# Step 2: in the meantime, assign indegrees for each node
# indegree means number of nodes point to the current node
# Step 3: 遍历n次，每一次都 go through all courses, find a node with indegree == 0
# if there is one, make this indegree = -1, and it's pointed nodes indegree -1
# if there is no indegree = 0, return false, means there is a closed loop

# TC: O(n^2)
# SC: O(n)
# Solution 2: DFS
# 实际上DFS快很多

# Solution 1
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for i in prerequisites:
            p = i[1]
            c = i[0]
            graph[p].append(c)
            indegrees[c] += 1

        n = numCourses
        path = []

        for i in range(n):  # 意思是要遍历n次
            zerodegree = 0  # 先假设没有 zerodegree
            for j in range(n):
                if indegrees[j] == 0:
                    zerodegree = 1
                    indegrees[j] = -1
                    for c in graph[j]:
                        indegrees[c] -= 1
                    path.append(j)
                    break

            if not zerodegree:
                return []
        return path



# Solution 2: DFS
    # Step 1: create a graph with edge nodes, using prerequisites
    # Step 2: 定义一个visited，对每一个点visited[i] = 0, 1, 2
    # 0: 还没有拜访
    # 1: 正在拜访
    # 2: 拜访过了，后面没有loop，是成功的
    # step 3: 从每一个点开始，一直往下走，如果下面的点的visited = 1，那就是当前正在visit的点，是loop。遇到0可继续往下走，遇到2，return true，直到遍历结束

# TC: O(n)：访问了每一个node一次
# SC: O(n)

# 注意：要return path[::-1], 因为在recursion的过程中，每一次是append的最后一个node

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # define a function to check step 3, call it dfs
        # return true: means no loop
        # return false: means there is a loop
        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            # 如果是0的话，当前就要开始访问了，所以给1
            visited[i] = 1
            for j in graph[i]:
                if dfs(j) == False:
                    return False
            # 都成功了，证明这点OK，给2
            visited[i] = 2
            path.append(i)
            return True

        # create a graph
        graph = collections.defaultdict(list)
        for i in prerequisites:
            p = i[1]
            c = i[0]
            graph[p].append(c)

        # loop every course in numCourses, determine if it is a loop
        path = []
        visited = [0] * numCourses
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return path[::-1]