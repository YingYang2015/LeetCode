# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

# recursion: O(2^n), too time consuming, does not pass leetcode
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 0 or n == 0:
#             return -1
#         if m == 1 or n == 1:
#             return 1
#         if m == 2 and n == 2:
#             return 2
#         return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)

# DP: 自下而上的方法

# Time complexity: O(M*N)
# Space complexity: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        r = [[1 for i in range(n)] for i in range(m)]

        if m == 0 or n == 0:
            return -1
        if m == 1 or n == 1:
            return 1

        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = r[i - 1][j] + r[i][j - 1]

        return r[m - 1][n - 1]



# def uniquePaths_test():
#     s = Solution()
#     assert s.uniquePaths(0,1) == -1
#     assert s.uniquePaths(0,0) == -1
#     assert s.uniquePaths(2,2) == 2
#     assert s.uniquePaths(3,2) == 3