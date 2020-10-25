# 3. Longest Substring Without Repeating Characters

# l: 左指针
# r：右指针
# c_dict 记录出现的letter的index
# 如果又出现了，
    # 如果原来的位置在现在的window里
        # 就把左指针移到上次出现的位置，把新的位置给这个letter
    # 如果原来的位置不在现在的window里
        # 需要把它update成现在的index
# 如果dict里没有：加进去

# 本来应该是 r-l+1的，因为k是出现了的位置，所以实际长度应该是r-(l+1)+1 =r-l

# test case example： "tmmzuxt"
# run a test case
# r
# l
# t:
# m:
# ...


# TC: O(N)
# SC: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len, c_dict = -1, 0, {}

        for r, value in enumerate(s):
            if value in c_dict.keys() and c_dict[value]>l: # 字符value在字典中 且 上次出现的下标大于当前长度的起始下标 (c_dict[value]>l 这个很关键, 不再看l之前的letter了，等同于把这部分dict删掉)
                l = c_dict[value]
                c_dict[value] = r
            else: # 这里只用else，可以把不在window里的字母，update成在window里的index
            # elif value not in c_dict.keys():
                c_dict[value] = r
                max_len = max(max_len, r-l)
        print(c_dict)
        return max_len