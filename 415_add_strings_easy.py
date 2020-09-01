

# Approach 1: Elementary Math
# Here we have two strings as input and asked not to convert them to integers. Digit-by-digit addition is the only option here.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0

        n1 = len(num1)-1
        n2 = len(num2)-1

        while (n1>=0 or n2>=0):
            r1 = ord(num1[n1]) - ord('0') if n1>=0 else 0
            r2 = ord(num2[n2]) - ord('0') if n2>=0 else 0

            value = (r1 + r2 + carry)%10
            carry = (r1 + r2 + carry)//10

            res.append(value)

            n1 -= 1
            n2 -= 1

        if carry != 0:
            res.append(carry)

        res = res[::-1]

        return ''.join(str(i) for i in res)


def addStrings_test():
    s = Solution()
    assert s.addStrings('1', '1') == '2'
    assert s.addStrings('15', '20') == '35'
    assert s.addStrings('105', '100') == '205'
    assert s.addStrings('1', '100') == '101'

if __name__ == '__main__':
    addStrings_test()