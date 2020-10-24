# 311  Sparse Matrix Multiplication
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

# 解题思路一：brutal force, 需要三重循环
# TC：O(N^3)
# 当遇到item是0的时候就不乘了
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in range(l):
                        if B[k][j]:
                            res[i][j] += A[i][k] * B[k][j]
        return res　　

# 解题思路二：encode-decode
# step 1: encode to dense matrics，把sparse matrix记录成一个dict，key：坐标，value：非0 item
# step 2： A, B encode, 只相乘非0项目，给新的matrix坐标
# step 3： decode成sparse matrix

class Solution(object):
    def encode(self, M):
        D = collections.defaultdict(list)
        r,c = len(M), len(M[0])
        for i in range(r):
            for j in range(c):
                if M[i][j]:
                    D[(i,j)] = M[i][j]
        return D

    def decode(self, D, r, c):
        M = [[0 for i in range(c)] for i in range(r)]
        for (i,j),val in D.items():
            M[i][j] = val

        return D

    def multiply(self, A, B):
        A_dense, B_dense = self.encode(A), self.encode(B)
        ans = collections.defaultdict(list)
        for (i,j) in A_dense.keys():
            for k in range(len(B[0])):
                if (j,k) in B_dense.keys():
                    ans[(i,k)] += A_dense[(i,j)] * B_dense[(j,k)]

        return self.decode(ans, len(A), len(B[0]))




