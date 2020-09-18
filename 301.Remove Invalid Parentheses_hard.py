# 301. Remove Invalid Parentheses
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# Note: The input string may contain letters other than the parentheses ( and ).
# 力扣：https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/bfsjian-dan-er-you-xiang-xi-de-pythonjiang-jie-by-/


# Solution: using BFS
# BFS 想象有不同的层
# 第一层就是原数组
# 第二层的话就是原数组删掉一个元素，每一个element是删掉其中一个元素
# 这里每一层是个set，来排除duplicate
# 在建的时候，如果发现本层已经有合法的了，就结束了，return所有的合法的
# 如果没有，就继续向下走
# 依次往更多的level走
# 注意：巧妙的利用filter（function， set）， 给出filtered set

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        # a function to determine if the string have only valid '()'
        def isValid(s):
            cnt = 0
            for i in s:
                if i == '(':
                    cnt += 1
                if i == ')':
                    cnt -= 1
                # 这个是考虑如果 ）就在左边开始的case
                if cnt <0:
                    return False

            return cnt == 0


        # construct the intital level: current_level
        current_level = {s}
        Valid = set()
        while s:
            # decide if current_level has valid string
            Valid = set(filter(isValid, current_level))
            # 如果valid不是空的，就return Valid_set
            if Valid:
                return Valid
            # if it is empty, construct the next level
            next_level = set()
            for i in current_level:
                item = list(i).copy()
                for j in range(len(item)):
                    if item[j] in ['(', ')']:
                        item.pop(j)
                        # set只能用add，add一个string
                        next_level.add(''.join(item))
                        item = list(i).copy()

            current_level = next_level

        if not Valid:
            return [""]
s= Solution()
s.removeInvalidParentheses("()())()")




