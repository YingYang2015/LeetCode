# 424. Longest Repeating Character Replacement
# 力扣： https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/python-hua-dong-chuang-kou-by-cui-jin-hao-_offic-2/

# Input:
# s = "ABAB", k = 2
# Output: 4
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.

# 解题思路：
# 用滑动窗口，左右指针
# l, r = 0, 0
# 一个dict记录当前在窗口里的每个字母连续的frequency： key：letter，value：frequency
# r先滑动，给dict[s[r]] += 1
# 当前的窗口大小是r-l+1， 如果 max_frequency + k >= r-l+1，
# 这个过程要maintain一个max_len = max(max_len, r-l+1)
# 证明窗口还没满，可以继续r+=1 来加入新的letter，看是否还可以加入maxfre
# 一旦 max_frequency + k < r-l+1, 说明窗口过大了，l+=1， 同时update dict[s[l]] -= 1
# return max_len

# TC: O(N)
# SC: O(N)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= 1:
            return n

        l, r, max_len, max_freq = 0, 0, 0, 0
        dict = collections.defaultdict(int)

        # 注意：这里要用for循环，不能用while
        for r in range(n):
            dict[s[r]] += 1
            max_freq = max(dict.values())
            if max_freq + k < r- l + 1:
                dict[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len