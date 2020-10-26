# 224 + . Basic Calculator
# 772. Basic Calculator III

# Solition:
# have one more stack to record the sign in front of '('
# '(' 进stack，遇到 '）'，就把前面的都加起来
# 注意 '）' 是末尾的case，加了个'e'，保证末尾的最后一个num还会再被calculate一遍
# TC： O（n)
# SC： O（n）

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        if s[-1] == ')':
            s = s+'e'
        stack = []
        sign = '+'

        ops = ['+', '-', '*', '/', ')', 'e']
        num = 0
        # 这是处理'('是第一个的情况
        sign_p = ['+']

        for i in range(len(s)):
            if s[i] not in ops and s[i] not in ['(', ')']:
                num = num * 10 + int(s[i])

            if s[i] == '(':
                stack.append(s[i])
                if i>0:
                    sign_p.append(s[i - 1])
                # 如果是‘（’ 相当于括号里重新算，所以sign和num都要初始
                sign, num = '+', 0

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
                #如果是正常的加减乘除，就重新给num 0， 如果是'('，num就是括号里计算出来的值
                sign, num = s[i],0

                if s[i] == ')':
                    while stack[-1] != '(':
                        t = stack.pop()
                        num += t
                    stack.pop()
                    sign = sign_p.pop()
        res = sum(stack)

        return res

s = Solution()
print(s.calculate("((((1*10)-(3*8))*3)*1)"))
