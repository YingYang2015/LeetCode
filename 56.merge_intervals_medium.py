# Given a collection of intervals, merge all overlapping intervals.

# Step 1: 先把原list 按照lower band都sort了
# step 2: 遍历每一个list，如果lower band小于前面list的higher band的话，就merge

# TC：O(NlogN + N) -> O(NlogN)： N, list length, 实际上是sort的复杂度
# SC： O(N)

# 需要注意的
# 1. sorted function 的用法
# 2. 一定要按x[0] 排序，因为lower band要从小到大 遍历的

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        if n < =1:
            return intervals

        ints = sorted(intervals, key=lambda x: x[0])

        new_ints = [ints[0]]
        i = 1

        print(ints)
        while i < n:
            if new_ints[-1][1] >= ints[i][0]:
                new_ints[-1][0] = new_ints[-1][0]

                new_ints[-1][1] = max(new_ints[-1][1], ints[i][1])

            elif new_ints[-1][1] < ints[i][0]:
                new_ints.append(ints[i])

            i += 1

        return new_ints