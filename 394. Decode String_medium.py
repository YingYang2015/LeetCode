# 394. Decode String

# example input
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# 解题思路
# 通过stack， 遍历s，
# 如果是number的话，就s.pop(), 如果也是number， 就*10+number形成一个number，放回stack
# 如果是[, 直接进入
# 如果是letter：直接进入
# 如果是], stack.pop(), 存在tmp里，一直到[
# pop最上面的number形成repeated list，放回stack
# return stack

# TC: O(N): 递归会更新索引，因此实际上还是一次遍历 s；
# SC: O(N), 极端情况下递归深度将会达到线性级别。


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        if n <= 3:
            return s

        stack = []

        tmp = []
        for i in s:
            if i == '[' or i.isalpha():
                stack.append(i)
            elif i.isdigit():
                if stack:
                    if stack[-1].isdigit():
                        i_pre = stack.pop()
                        # 注意：这要先转换成int，然后转化成str再放到stack里，isdigit只能判断str
                        i = int(i_pre) * 10 + int(i)
                stack.append(str(i))
            elif i == ']':
                while stack[-1] != '[':
                    l = stack.pop()
                    tmp.append(l)
                tmp = tmp[::-1]

                # pop [
                stack.pop()

                tmp = tmp * int(stack.pop())
                stack = stack + tmp
                tmp = []

        return ''.join(stack)