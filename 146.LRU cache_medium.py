# 146. LRU Cache

# 力扣：https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/

# Solution: 利用hash table，and OrderedDict(), it is like linked list
# 每次put or get，take the key to the end, then pop the head node when the length exceed capccity

# TC: O(1)
# SC: O(1)

# 做unit test
# 考虑，一直插入的情况
# get没有的值的情况
# get存在值的情况


import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.n = capacity

    def get(self, key: int) -> int:

        if key in self.dict.keys():
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        self.dict[key] = value
        self.dict.move_to_end(key)

        if len(self.dict) > self.n:
            self.dict.popitem(last=False)