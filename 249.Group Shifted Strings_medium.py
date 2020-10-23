# 249 Group Shifted Strings

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Return:
#
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

# 解题思路：
# construct a hashtable, key is original number of each string, value is all the strings
# what is the key?
# string:           'abc', 'bcd'
# number:           '123', '234'   -- minus the first number
# original number:  '012', '012'
# so these two can go to the same key in the hashtable
# Caution: need to deal with the negative case: for example
# 'zab'
# '0, -25, -24'
# we can %26, to take find the real number

# TC: O(N)
# SC: O(N)

# need a function to construct the key
import collections
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def hashkey(s):
            return tuple([ord(c) - ord(s[1])%26 for c in s])

        hashtable = collections.defaultdict(list)
        for s in strings:
            hashtable[hashkey(s)].append(s)

        return list(hashtable.values())