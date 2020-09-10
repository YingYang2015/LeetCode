# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.
#
# The answer is guaranteed to be unique (except for the order that it is in.)


# https://leetcode.com/problems/k-closest-points-to-origin/solution/


# Method 1: sort with python function
# TC: O(nLogn)

# method 2:         # Solution: minheap
#         # translate to negateive distance, means to find the top highest K
#
#         # step 1: create a dictionary with point index as the key, distance as the value
#         # Step 2: create a minheap with the first k points
#         # Step 3: from k+1 to n points, everytime compare the point with the top node in the maxheap. I
#             #If it is smaller, disgard, if it is bigger or equal, replace the top node with it.
#         # Step 4: transform the min to a list and output.
# TC: O(nLogK)

# Method 3: divide and Conquer


# TC: O(NlogN)
# SC: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[0:K]




# TC: O(NlogN)
# SC: O(N)
# 注意：dic key can be a list, must be tuple
# dic key should be the list element instead of the euclidean distance
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = {}
        for i in points:
            dic[tuple(i)] = i[0] ** 2 + i[1] ** 2

        l = list(dic.values())
        l.sort()

        return [i[0] for i in dic.items() if i[1] in l[0:K]]

# Method 2: minHeap
class Solution(object):
    def kClosest(self, points, K):
        # Solution: minheap
        # translate to negateive distance, means to find the top highest K

        # step 1: create a dictionary with point index as the key, distance as the value
        # Step 2: create a minheap with the first k points
        # Step 3: from k+1 to n points, everytime compare the point with the top node in the maxheap. I
            #If it is smaller, disgard, if it is bigger or equal, replace the top node with it.
        # Step 4: transform the min to a list and output.
        dict = {}
        n = len(points)

        l1 = [[-(points[i][0] ** 2 + points[i][1] ** 2), i] for i in range(n)]

        h = l1[0:K]
        heapq.heapify(h)

        for i in range(K, n):
            top_node = heapq.heappop(h)

            if l1[i][0] >= top_node[0]:
                heapq.heappush(h, l1[i])
            else:
                heapq.heappush(h, top_node)
        res = []
        for i in range(K):
            res.append(points[heapq.heappop(h)[1]])
        return res