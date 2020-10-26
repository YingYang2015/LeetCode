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
# Time Complexity: O(max(n1,n2))
# space complexity: O(max(n1,n2)), because the length of the final string is at most max(n1,n2)+1
# Here we have two strings as input and asked not to convert them to integers. Digit-by-digit addition is the only option here.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = [], 0
        n1, n2 = len(a) - 1, len(b) - 1

        while n1 >= 0 or n2 >= 0 or carry > 0:
            r1 = ord(a[n1]) - ord('0') if n1 >= 0 else 0
            r2 = ord(b[n2]) - ord('0') if n2 >= 0 else 0

            value = (r1 + r2 + carry) % 2
            carry = (r1 + r2 + carry) // 2

            res.append(str(value))
            n1 -= 1
            n2 -= 1

        res = res[::-1]
        # print(res)
        return ''.join(res)




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