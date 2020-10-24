
# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
#
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
#
# More formally, the probability of picking index i is w[i] / sum(w).

# Solution: Use presum
# 力扣解释：https://leetcode-cn.com/problems/random-pick-with-sweight/solution/ji-he-jie-shi-by-powcai/

# 随机generate一个数，看他落在了哪个区间,return这个区间的lower index
# 因为每一个区间的长度不同，就代表了probability

class Solution:
    def __init__(self, w: List[int]):
        self.pre_sum_list = []
        pre_sum = 0
        for i in range(len(w)):
            pre_sum += w[i]
            self.pre_sum_list.append(pre_sum)
        self.w = w
        self.total_sum = pre_sum

    def pickIndex(self) -> int:
        num = random.randint(1, self.total_sum)
        # num = self.total_sum * random.random()
        l = 0
        r = len(self.pre_sum_list) - 1

        while l <= r:
            mid = int((l + r) / 2)
            if num > self.pre_sum_list[mid]:
                l = mid + 1
            if num < self.pre_sum_list[mid]:
                r = mid - 1
            if num == self.pre_sum_list[mid]:
                return mid

        return l



