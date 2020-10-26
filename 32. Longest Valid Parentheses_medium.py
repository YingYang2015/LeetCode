# 32. Longest Valid Parentheses

# 解题思路：
# -1 先进stack, last_matched_index
# the maximum length is max(max_len, last_matched_index - top index in stack)
# if stack is empty, use -1 as top index stack

# 利用stack， with (idx)，遍历s，看每次进入的是否能match (),
# len就是当前的current_len = index - stack pop之后里面最上面的index

# maintain一个max_len = max(max_len, current_len)

# TC: O(N)
# SC: O(N)


# 这种也可以，就在stack里maintain一个index
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res

# # 这种也可以，就在stack里也放上了value， maintain一个index
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:

#         if not s:
#             return 0

#         max_len = 0
#         stack = [(-1, '')]

#         for i, v in enumerate(s):
#             if v == '(':
#                 stack.append((i,v))
#             elif v == ')':
#                 if not stack:
#                     stack.append((i,v))
#                 else:
#                     index_pre, v_pre = stack.pop()
#                     if v_pre == '(':
#                         cur_len = i - stack[-1][0]
#                         max_len = max(max_len, cur_len)
#                     else:
#                         stack.append((i,v))
#         return max_len