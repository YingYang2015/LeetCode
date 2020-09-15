# 986. Interval List Intersections

# https://leetcode.com/problems/interval-list-intersections/

# Solution:
# have two pointers i, j
# start with i = 0, j = 0
# compare A[i], B[j]
# if there is an intersect, append the intersect with the result
# check the end point of A[i], and B[i], since both A and B are the sorted list
# you can remove the interval with the smaller end point, and keep moving forward

# TC: O(M+N)
# SC: O(M+N)

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        if not A or not B:
            return []

        res = []
        i = 0
        j = 0

        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])

            if low <= high:
                res.append([low, high])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return res


