from typing import List
import collections
# Question:
#    - input: array of integers,
#    - out: find all pairs of integers that sum up to a particular number K


# Solution:
# Step 1: array of integer to a hash table: key: value, value: index
# Step 2: find K - value in the hashtable, and return index

# [2, 5, 6, 4, 3], 6
# 2: 0
# 5: 1
# 6: 2
# 4: 3
# 3: 4

class Solution:
    def pairSum(self, a: List[int], k: int) -> List:
        dict = collections.defaultdict(list)

        pair_list = []

        for i, v in enumerate(a):
            if k - v in dict.keys():
                pair_list.append([a[i], a[dict[k-v]]])
            else:
                dict[v] = i

        return pair_list

# TC: O(N)

s = Solution()
a = [2, 5, 6, 4, 3, 3]
k = 6
print(s.pairSum(a, k))
