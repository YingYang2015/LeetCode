# LeetCode 1428. Leftmost Column with at Least a One
# 没有在leetcode里跑，因为premium

# 题目描述：
# (This problem is an interactive problem.)
#
# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn’t exist, return -1.
#
# You can’t access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
#
# BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
#
# For custom testing purposes you’re given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

#解题思路
# 思路1：线性查找：
# 从右下角开始，向左找找到最左边的1，记录坐标（res），然后向上找，如果是0继续向上，如果是1，向左，更新res
#TC :O(m+n)
#SC：O(1)

# 思路2：每一行binary search：
# 从最下面的行开始，先找到最左边的1，记录坐标res，然后filter lines只有在这个坐标是1的，继续binary search
#TC :O(nlogm)
#SC：O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        if n == 0 or m == 0:
            return -1

        row = n-1
        column = n-1
        while row>=0 and column >=0:
            while binaryMatrix.get(row, column) == 1:
                column -= 1
            while binaryMatrix.get(row, column) == 0:
                row -= 1

        if column == n-1 and row == 0:
            return -1
        else:
            return column+1



# 二分查找
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        def binary_search(binaryMatrix, row):
            n = len(s)
            r = n
            l = 0
            while l < mid:
                mid = (l+r)//2 # odd: mid index: # even: the bigger one in two middle ones
                if binaryMatrix.get(row, mid) == 1:
                    r = mid
                elif binaryMatrix.get(row, mid) == 0:
                    l = mid
            if binaryMatrix.get(row, r) == 0:
                return -1
            else:
                return r

        n, m = BinaryMatrix.dimensions()
        min_c = -1
        for row in range(n):
            c = binary_search(binaryMatrix, row)
            min_c = min(min_c, c)

        return min_c




