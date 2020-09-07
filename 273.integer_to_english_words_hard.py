# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# # 需要注意的地方
# 1. return zero
# 2. one_trans 1-9, 2_less_20: 10-19, 2_higher_20: 20:90
# 3. two, three, 两个function都要return 整个小于3位数，小于2位数的书写，之后就只用three了
# 4. 注意最后的result部分的空格书写，而且最后四个是有顺序的

# TC：O(N): N is the number of digits
# SC：O(1)
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        one_trans = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        two_less_20_trans = switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }

        two_higher_20_trans = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }

        def one(num):
            return one_trans[num]

        def two(num):
            if num < 10:
                return one(num)
            elif num < 20:
                return two_less_20_trans[num]
            elif num >= 20:
                if num % 10 == 0:
                    return two_higher_20_trans[num//10]
                else:
                    return two_higher_20_trans[num//10] + ' ' +  one_trans[num %10]

        def three(num):
            if num >= 100:
                n_3 = num//100
                n_2 = num % 100
                if n_2 == 0:
                    return one(n_3) +' Hundred'
                else:
                    return one(n_3) +' Hundred '+ two(n_2)
            elif num >= 10:
                return two(num)
            elif num >= 1:
                return one(num)
            elif num == 0:
                return ''

        def billion_words(billion):
            if billion:
                return three(billion) + ' Billion'
            else:
                return ''

        def million_words(million):
            if million:
                return three(million) + ' Million'
            else:
                return ''
        def thousand_words(thousand):
            if thousand:
                return three(thousand) + ' Thousand'
            else:
                return ''



        one_billion = 1000000000
        one_million = 1000000
        one_thousand = 1000
        billion = num//one_billion
        million = (num - billion * one_billion )//one_million
        thousand = (num - billion * one_billion - million * one_million )//one_thousand
        rest = (num - billion * one_billion - million * one_million -thousand * one_thousand)
        print(billion, million, thousand, rest)

        result = ''
        if billion:
            result = billion_words(billion)

        if million:
            result += ' ' if result else ''
            result += million_words(million)

        if thousand:
            result += ' ' if result else ''
            result += thousand_words(thousand)

        if rest:
            result += ' ' if result else ''
            result += three(rest)
