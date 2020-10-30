# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#


# Note: 必须要每两个words相比
# 之前想过先对比在letter level，是不对的，因为必须要先第一个小于第二个才可以
# 几个rule：
    # 1.要先对比letter，一直一样的话，最后看长度
# TC: O(n*m)
# SC: O(1)


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        # step 1: get a dictionary
        #order = '0' + order
        letter_ord = {order[i]: i for i in range(len(order))}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for i in range(min(len(word1), len(word2))):
                o1 = letter_ord[word1[i]]
                o2 = letter_ord[word2[i]]
                print(o1, o2)
                if o1 > o2:
                    return False
                if o1 < o2:
                    break
            if o1 == o2 and len(word1) > len(word2):
                return False

        return True



words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
s = Solution()
print(s.isAlienSorted(words, order))