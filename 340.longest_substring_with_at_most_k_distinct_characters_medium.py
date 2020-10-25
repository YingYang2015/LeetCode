# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

# 解题思路
# have a left and right pointer, starting from 0
# move right first
    # if the number of disctinct character n<=k, keep moving right
    # if n>k, move left to reduce it to k

# How to move the left curve
# Method 1:
    # use a hashmap, which keeps the letters of the curent substring, key is the letter, value is the right position
    # if n > k, you need to remove all letters before the lowest right position.
    # hence find the minimum right postion of all keys index = min(hash.values()), this is the index the left should move to and plus 1
    # left = min(hash.values())
    # then remove this key value pare from hashmap: del hashmap[s[index]]

# TC: O(N)
# SC: O(k)
# Method 1 快
# Method 2:
    # also use hashmap, which keeps the letters of the current substring
    # key is the letter, value is the number of time in the string
    # n = len(hashmap)
    # everytime move, update the value, calcuate n.
    # if the value == 0, pop this item
    # calculate n

# TC: O(N)
# SC: O(k)

# method 1:

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)

        # 这个部分 要先 K == 0
        if k == 0:
            return 0
        if n <= 1:
            return n

        left, right, max_len = 0,0,0
        hashmap = defaultdict()

        # 注意这个部分，要先把right + 1，然后再check
        while left < n and right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) > k:
                index = min(hashmap.values())
                del hashmap[s[index]]
                left = index + 1
            max_len = max(max_len, right - left)
        return max_len




class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # n is the number of distinct characters in the substring
        # two pointers,
        # one in the front moving forward when n<=K
        # one in the back, moving forward when n>k
        n = len(s)
        if k == 0:
            return 0
        if n <= 1:
            return n

        p1, p2, max_len = 0,0,0

        dic = collections.defaultdict(int)
        dic[s[0]] = 1
        num_char = len(dic)

        while p1 < n and p2 < n:
            if num_char <= k:
                max_len = max(max_len, len(s[p1:p2 + 1]))
                p2 += 1
                if p2 < n:
                    dic[s[p2]] += 1
            elif num_char > k:
                dic[s[p1]] -= 1
                if 0 in list(dic.values()):
                    dic.pop(list(dic.keys())[list(dic.values()).index(0)])
                p1 += 1
            num_char = len(dic)

        return max_len