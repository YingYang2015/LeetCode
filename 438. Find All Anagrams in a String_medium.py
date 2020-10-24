# 438. Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# Input: s: "cbaebabacd" p: "abc"
# Output: [0, 6]

# 解题思路：
# 利用hashtable，和滑动窗口
# 建立一个hashtable，key是26个字母，value是当前窗口里的letter的数目
# 窗口是 p的长度
# hash_p, 就是记录p

# 每滑动一次窗口，如果hash_p = hash_w, 就返回窗口的最小index
# 力扣： https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/duo-chong-si-lu-by-powcai-3/
#TC：O(N)
#SC：O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        hash_w = collections.defaultdict(int)
        hash_p = collections.defaultdict(int)
        for i in range(97, 97 + 26):
            hash_w[chr(i)] = 0
            hash_p[chr(i)] = 0
        for j in p:
            hash_p[j] += 1

        l, r = 0, len(p) - 1

        for i in range(l, r):
            hash_w[s[i]] += 1

        res = []
        while r < len(s):
            hash_w[s[r]] += 1
            if hash_w == hash_p:
                res.append(l)
            hash_w[s[l]] -= 1
            r += 1
            l += 1

        return res

