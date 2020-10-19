# 621. Task Scheduler

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# 思路：填桶 https://leetcode-cn.com/problems/task-scheduler/solution/tian-tong-si-lu-you-tu-kan-wan-jiu-dong-by-mei-jia/
# bucket size: n+1
# number of the max number of same task: k
# 有两种情况
# 1. 当每个桶填不满时：（n+1）* (k-1) + num(tasks = k)
# 2. 当桶填满的时候：最短的时间就是number of totak tasks
# 所以答案就是取两种情况的最大值

# TC: O(N), N: number of tasks
# SC: O(N)
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # key: task, value: number of tasks
        dict = collections.Counter(tasks)

        cnt = list(dict.values())
        k = max(cnt)
        res_tasks = sum([1 for i in cnt if i == k])
        ans = max(len(tasks), (n + 1) * (k - 1) + res_tasks)
        return ans
