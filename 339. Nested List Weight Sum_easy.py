# 339. Nested List Weight Sum

# 不太容易懂，recursion多看一下
# TC：O(N), where N is the total number of nested elements in the input list.
# For example, the list [ [[[[1]]]], 2 ] contains 4 nested lists and 2 nested integers (1 and 2）
# so N=6.
# SC： at most O(D) recursive calls are placed on the stack,
# D is the maximum level of nesting in the input.
# For example, D=2 for the input [[1,1],2,[1,1]], and D=3 for the input [1,[4,[6]]].


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def flatten_list(nestedList, depth):
            weight_sum = 0
            for integer in nestedList:
                if integer.isInteger():
                    weight_sum += integer.getInteger() * depth
                else:
                    weight_sum += flatten_list(integer.getList(), depth + 1)
            return weight_sum

        return flatten_list(nestedList, 1)