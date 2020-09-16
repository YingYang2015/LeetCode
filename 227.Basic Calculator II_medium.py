# 227. Basic Calculator II

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# 力扣 https://leetcode-cn.com/problems/basic-calculator-ii/solution/zhan-by-elevenxx/

# 利用stack
# step 1: 初始化empty stack，给+对第一个number
# step 2：calculate这个number
# step 3：如果遇到了op
    # 如果前面的sign是+，-，就把num进stack
    # 如果前面的sign是* /， 就把stack.pop, 进行运算，再放回去
# 最后初始化num，和sign = s[i]
# sum stack就是最后的结果

# TC：O(n)
# SC: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        sign = '+'

        ops = ['+', '-', '*', '/']
        num = 0

        for i in range(len(s)):
            if s[i] not in ops:
                num = num * 10 + int(s[i])
                # print(num, sign)
            if s[i] in ops or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    tmp = stack.pop() * num
                    stack.append(tmp)
                elif sign == '/':
                    tmp = int(stack.pop() / num)
                    stack.append(tmp)

                sign = s[i]
                num = 0

        res = sum(stack)

        return res







class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace(' ', '')
        s = list(s)

        def get_num(s, index):
            operater = ['+', '-', '*', '/']

            max_index = index + 1
            min_index = index - 1
            while s[max_index] not in operater:
                max_index += 1
                if max_index == len(s):
                    break

            while s[min_index] not in operater:
                if min_index >= 0:
                    min_index -= 1
                else:
                    break
            s1 = int(''.join(s[min_index + 1:index]))
            s2 = int(''.join(s[index + 1:max_index]))
            return s1, s2, min_index + 1, max_index

        while s:
            if '*' in s or '/' in s:
                index_m = s.index('*') if '*' in s else float('inf')
                index_d = s.index('/') if '/' in s else float('inf')

                index = min(index_m, index_d)
                s1, s2, min_index, max_index = get_num(s, index)
                if s[index] == '*':
                    tmp = s1 * s2
                if s[index] == '/':
                    tmp = int(s1 / s2)
                s[min_index:max_index] = str(tmp)

            else:
                break

        while s:
            if '+' in s or '-' in s:
                index_p = s.index('+') if '+' in s else float('inf')
                index_s = s.index('-') if '-' in s else float('inf')

                if index_s == 0 and ('+' not in s[1:] and '-' not in s[1:]):
                    break
                elif index_s == 0 and ('+' in s[1:] or '-' in s[1:]):
                    index_n = min(s[1:].index('+') if '+' in s[1:] else float('inf'),
                                  s[1:].index('-') if '-' in s[1:] else float('inf')) + 1
                    s1, s2, min_index, max_index = get_num(s, index_n)
                    if s[index_n] == '+':
                        tmp_p = -s1 + s2
                    if s[index_n] == '-':
                        tmp_p = -s1 - s2
                    s[min_index - 1:max_index] = str(tmp_p)
                else:
                    index = min(index_p, index_s)
                    s1, s2, min_index, max_index = get_num(s, index)
                    if s[index] == '+':
                        tmp_p = s1 + s2
                    if s[index] == '-':
                        tmp_p = s1 - s2
                    s[min_index:max_index] = str(tmp_p)
            else:
                break
        return ''.join(s)