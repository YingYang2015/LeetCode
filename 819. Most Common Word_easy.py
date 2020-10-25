# 819. Most Common Word

# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

# one pass
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_p = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        # 记得要先split
        p_list = new_p.split()
        count = collections.defaultdict(int)

        max_count = 0
        for i in p_list:
            if i not in banned:
                count[i.lower()] += 1
                if count[i.lower()] > max_count:
                    res = i
                    max_count = max(max_count, count[i.lower()])

        return res


# another solution
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_p = ''.join([i.lower() if i.isalnum() else ' ' for i in paragraph])
        p_list = new_p.split()

        count_dict = collections.Counter(p_list)

        # for i in count_dict.keys():
        for i in banned:
            del count_dict[i]

        l_key = list(count_dict.keys())
        l_count = list(count_dict.values())

        return l_key[l_count.index(max(l_count))]


