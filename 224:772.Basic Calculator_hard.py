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
        print(s)
        stack = []
        sign = '+'

        ops = ['+', '-', '*', '/', ')', 'e']
        num = 0
        num_p = 0
        sign_p = []

        for i in range(len(s)):
            print(stack, s[i], num, sign)
            if s[i] not in ops and s[i] not in ['(', ')']:
                num = num * 10 + int(s[i])
                # print(num, sign)

            if s[i] == '(':
                stack.append(s[i])
                if i-1>=0 and s[i - 1] != '(':
                        sign_p.append(s[i - 1])
                else:
                    sign_p.append('+')

                sign = '+'
                num = 0
                print('sign_p', sign_p)

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

                if s[i] == ')':
                    t = 0
                    while t != '(':
                        num = num + int(t)
                        t = stack.pop()
                    sign = sign_p.pop()

                    print(sign)

        res = sum(stack)

        return res

s = Solution()
print(s.calculate("((((1*10)-(3*8))*3)*1)"))
