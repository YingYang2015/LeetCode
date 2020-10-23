# 65. Valid Number

# Validate if a given string can be interpreted as a decimal number.

# Some requirements

# letter: if there is letter in there, return False
# number: there must be a number, otherwise, False (number_show_up)
# e:
# e can't be the first one or last one,
# if no number before, False (num_show_up)
# if no number after, False (num_show_up)
# if e already exists, false (e_show_up)
# sign
# first one
# or before is a 'e'
# . dot
# if dot already exists, False
# if it is after e, false
# space:
# only can occur in front or in the end
# use s = s.strip() to remove space in front and the end
# anything showup again is False
# integer can be interpreted as decimal number?

# 通过一个 num_show_up来统筹现在是否有number了，在处理e的时候比较特殊，如果e合法的话给num_show_up = False, 如果后面还有num的，if c.isdigit():会帮助update成True
# 最后return num_show_up，因为前面的判断是rule out了所有False的情况，都rule out之后，还有number的话就是True了
# TC： O（N）
# SC： O（1）

class Solution:
    def isNumber(self, s: str) -> bool:
        # 注意：这里把前后的space都删掉了，关键步骤
        s = s.strip()
        n = len(s)

        e_show_up, dot_show_up, num_show_up = False, False, False

        for i in range(n):
            c = s[i]
            if c.isdigit():
                num_show_up = True
            elif c in ('+', '-'):
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            elif c.isalpha():
                return False
            elif c == ' ':
                return False

        return num_show_up