# 791. Custom Sort String

# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
# Return any permutation of T (as a string) that satisfies this property.

# Solution: 利用了collectons.counter(T), 自动把T里的字母count了

# TC: O(S.len+T.len)
# SC: O(C)
class Solution:
    def customSortString(self, S: str, T: str) -> str:

        t_count = collections.Counter(T)

        t1 = [''] * len(S)
        t2 = []
        for i in t_count.keys():
            if i in S:
                t1[S.index(i)] = [i] * t_count[i]
            else:
                t2.append([i] * t_count[i])

        new_t1 = []
        new_t2 = []

        for i in t1:
            new_t1 += i
        for i in t2:
            new_t2 += i

        return ''.join(new_t1 + new_t2)
