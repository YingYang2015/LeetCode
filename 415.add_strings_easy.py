# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Approach 1: Elementary Math
# Time Complexity: O(max(n1,n2))
# space complexity: O(max(n1,n2)), because the length of the final string is at most max(n1,n2)+1
# Here we have two strings as input and asked not to convert them to integers. Digit-by-digit addition is the only option here.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = [], 0
        n1, n2= len(num1)-1, len(num2)-1

        while n1>=0 or n2>=0 or carry>0:
            r1 = ord(num1[n1]) - ord('0') if n1>=0 else 0
            r2 = ord(num2[n2]) - ord('0') if n2>=0 else 0

            value = (r1 + r2 + carry)%10
            carry = (r1 + r2 + carry)//10
            res.append(value)
            n1 -= 1
            n2 -= 1

        res = res[::-1]
        return ''.join(str(i) for i in res)


def addStrings_test():
    s = Solution()
    # assert s.addStrings('1', '1') == '2'
    # assert s.addStrings('15', '20') == '35'
    # assert s.addStrings('105', '100') == '205'
    assert s.addStrings('1', '1000') == '1001'

if __name__ == '__main__':
    addStrings_test()



# Follow up: what if there is decimals
# step 1: find the the index of decimal
# step 2: pad number of digits after the decimal the same for two strings with 0
# step 3: modify the previous function, leave decimal add to be '.'
# then report the data

class Solution:
    class Solution:
        def addStringsInt(self, num1: str, num2: str) -> str:
            res, carry = [], 0
            n1, n2 = len(num1) - 1, len(num2) - 1

            while n1 >= 0 or n2 >= 0 or carry > 0:
                num1_val = num1[n1] if n1 >= 0 else '0'
                num2_val = num2[n2] if n2 >= 0 else '0'
                if num1_val != '.' and num2_val != '.':
                    r1 = ord(num1_val) - ord('0')
                    r2 = ord(num2_val) - ord('0')
                    value = (r1 + r2 + carry) % 10
                    carry = (r1 + r2 + carry) // 10
                else:
                    value = '.'
                res.append(value)
                n1 -= 1
                n2 -= 1

            res = res[::-1]
            return ''.join(str(i) for i in res)

    def addStrings(self, num1: str, num2: str) -> str:

        n1 = len(num1)
        n2 = len(num2)

        dot_index1 = [num1.index('.')] if '.' in num1 else []
        dot_index2 = [num2.index('.')] if '.' in num1 else []

        # dot_index1 is not empty, but dot_index2 is empty
        if dot_index1 or dot_index2:
            d_num1 = list(num1[dot_index1[0]+1 :]) if dot_index1 else []
            d_num2 = list(num2[dot_index2[0]+1 :]) if dot_index2 else []

            dn1 = len(d_num1)
            dn2 = len(d_num2)
            if dn1 > dn2:
                num2 = list(num2) + ['0' for i in range(dn1 - dn2)]
            elif dn2 > dn1:
                num1 = list(num1) + ['0' for i in range(dn2 - dn1)]

        return self.addStringsInt(num1, num2)

def addStrings_test():
    s = Solution()
    assert s.addStrings('0.100', '100000.121') == '100000.221'
    assert s.addStrings('1', '1') == '2'
    assert s.addStrings('15', '20') == '35'
    assert s.addStrings('105', '100') == '205'
    assert s.addStrings('1', '100') == '101'

if __name__ == '__main__':
    addStrings_test()