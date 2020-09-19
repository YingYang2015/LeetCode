# 13. Roman to Integer


# Solution 1
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000,
               }

        dic_special = {'IV': 4,
                       'IX': 9,
                       'XL': 40,
                       'XC': 90,
                       'CD': 400,
                       'CM': 900,
               }

        s = str(s)
        num = 0

        j = 0
        while j < len(s):
            if s[j:j+1+1] in dic_special.keys():
                num += dic_special[s[j:j+1+1]]
                j += 2
            else:
                num += dic[s[j]]
                j += 1
        return num

obj = Solution()
print(obj.romanToInt('XX'))

# Solution 2
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000,
               }

        s = str(s)
        output_sum = 0
        for i in range(0, len(s) - 1):
            print("i is ",i)
            if dic[s[i]] < dic[s[i+1]]:
                output_sum -= dic[s[i]]
            else:
                output_sum += dic[s[i]]
            print(output_sum)
        return output_sum + dic[s[-1]]


# Solution 3:
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        pairs = collections.defaultdict(list)
        pairs['I'] = ['V', 'X']
        pairs['X'] = ['L', 'C']
        pairs['C'] = ['D', 'M']

        num = 0
        n = len(s)
        for i in range(n - 1):
            if s[i + 1] in pairs[s[i]]:
                num -= values[s[i]]
            else:
                num += values[s[i]]

        num += values[s[n - 1]]

        return num