# 398. Random Pick Index

# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# 解题思路1：
# step 1: 把每个value的所有index放在一个dict里
# step 2：从这个dict[value], randomly 选一个index
# TC： O（N）把所有index放到dict里complexity
# SC： O(N): dict的space，但是这种方式也很占用空间
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dict = collections.defaultdict(list)

        for i in range(len(self.nums)):
            self.dict[self.nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])

# 解题思路2：
# https://leetcode-cn.com/problems/random-pick-index/solution/xu-shui-chi-chou-yang-wen-ti-by-an-xin-9/
# 通过蓄水池抽样的方法: Reservior sampling
# go through the list, 遇到target， cnt+=1
# 每次遇到的时候，给一个概率，如果是 < 1/cnt,就抽这个index, # 以某一概率(1/count)抽样
# TC： O(N)
# SC： O(1)

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = -1
        cnt = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, cnt)<1:
                    res = i
                cnt +=1
        return res