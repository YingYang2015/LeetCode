# 242. Valid Anagram

# TC: O(n): n is the length of s
# SC: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hash(s):
            hash_s = collections.defaultdict(int)
            for i in s:
                hash_s[i] += 1
            return hash_s

        hash_s = hash(s)
        hash_t = hash(t)

        return hash_s == hash_t