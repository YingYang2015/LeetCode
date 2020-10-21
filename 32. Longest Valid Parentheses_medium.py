# 32. Longest Valid Parentheses

# 解题思路：
# -1 先进stack, last_matched_index
# the maximum length is max(max_len, last_matched_index - top index in stack)
# if stack is empty, use -1 as top index stack

# top_index
# cur_index

# 利用stack，遍历s，看每次进入的是否能match (),
# if match: update cur_index,
#     stack.pop()
#     if stack:
#         top_index= stack[-1]
#     elif not stack:
#         top_index = -1
#     current_len = cur_index - top_index
# maintain一个max_len = max(max_len, current_len)

# TC: O(N)
# SC: O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if not s:
            return 0
        max_len = 0
        stack = [(-1, '')]
        for i, v in enumerate(s):
            if v == '(':
                stack.append((i, v))
            elif v == ')':
                if not stack:
                    stack.append((i, v))
                else:
                    index_pre, v_pre = stack.pop()
                    if v_pre == '(':
                        cur_len = i - stack[-1][0]
                        max_len = max(max_len, cur_len)
                    else:
                        stack.append((i, v))
        return max_len