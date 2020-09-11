# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

# Solution: element wise sum
# TC: O(max(M, N))
# SC: O(max(M, N))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        i = n - 1
        res = []
        carry = 0
        while i >= 0:
            tmp = int(a[i]) + int(b[i]) + carry
            carry = tmp // 2
            num = tmp % 2

            res.append(str(num))
            i -= 1

        if carry > 0:
            res.append(str(carry))

        res = res[::-1]

        return "".join(res)