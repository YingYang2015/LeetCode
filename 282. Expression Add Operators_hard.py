# 282. Expression Add Operators

# 不是自己写的，要看一看
# BackTracking


# procedure recurse(digits, index, expression):
# 2.     if we have reached the end of the string:
# 3.         if the expression evaluates to the target:
# 4.             Valid Expression found!
# 5.     else:
# 6.         try out operator 'NO OP' and recurse
# 7.         try out operator * and recurse
# 8.         try out operator + and recurse
# 9.         try out operator - and recurse


# TC:O(N*4^N): At every step along the way, we consider exactly 4 different choices or 4 different recursive paths. The base case is when the value of index reaches
# N i.e. the length of the nums array. Hence, our complexity would be
# SC: O(N)




class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            # current_operand 是在
            if index == N:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    # 从1开始是因为0是+
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            # 如果是相加的话，value就是原来的value+current_operand, 就是把当前的value加了
            # 因为进recurse的时候是先evaluate value是不是到了
            # 这样的话进recurse的时候，
            # 1. current_operand就是0了，因为已经加过了，recurse里的current_op 就是num[index]了
            # 2. pre_operand就变成了current_operand，pre只matter for 乘法
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand  , string)
            # pop的意思就是，我可以加，加完了，拿走，然后还可以减，下面
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:
                # SUBTRACTION
                string.append('-'); string.append(str_op)
                print('SUBTRACTION')
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                print('MULTIPLICATION')
                recurse(index + 1, current_operand * prev_operand, 0,
                        value - prev_operand + (current_operand * prev_operand), string)
                # 假设以前已经加了，所以把以前的pre减掉，因为要用pre来乘
                string.pop();string.pop()

        # index, prev_operand, current_operand, value, string
        recurse(0, 0, 0, 0, [])



        return answers



num = "12"
target = 3
s = Solution()
print(s.addOperators(num, target))
