# 29. Divide Two Integers

# 解题思路
# brutal force: 就在dividend里一直减divisor，直到负数，记录减了几次，但是太慢了，如果dividend很大，divisor很小的话
# 优化：
# 开始减d = divisor*2， 再减d*2， 一直下去，这样减的就快，如果一旦负数了，回来，减divisor重新计数
# 考虑一下sign，先create一个出来
# TC: O(logN)
# SC: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res, i, d = 0, 0, divisor

        while dividend >= divisor:
            dividend -= d
            if dividend >= 0:
                res += 2 ** i
                i += 1
                d += d
            else:
                dividend += d
                d,i = divisor,0
        res = sign * res

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < -2 ** 31:
            return -2 ** 31
        return res
