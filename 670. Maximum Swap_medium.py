# 670. Maximum Swap

# Solution:
# step 1. 先用一个dict来 记录数组里每一个数值的最后一个index
# step 2. 遍历数组，对每一个值，来和后面的最大的值来比，
# # 如果有比这个大的，就把这个最大值的最后一个位置（last index）和当前的值做swap，结束


# TC: O(N)： 因为只遍历了一次
# SC: O(1)
# Solution 1: greedy


class Solution:
    def maximumSwap(self, num: int) -> int:

        # step 1. 先用一个dict来 记录数组里每一个数值的最后一个index
        l = list(str(num))
        last = {x: i for i,x in enumerate(l)}
        n = len(l)
        # step 2. 遍历数组，对每一个值，来和后面的最大的值来比，
        # # 如果有比这个大的，就把这个最大值的最后一个位置（last index）和当前的值做swap，结束
        for i in range(n-1):
            max_l_post =max(l[i+1:])
            if l[i] < max_l_post:
                l[i], l[last[max_l_post]] = l[last[max_l_post]], l[i]
                return ''.join(l)
        return num

# Solution 2: Brutal force
# 答案写的
def maximumSwap(self, num):
    A = list(str(num))
    ans = A[:]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans: ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))