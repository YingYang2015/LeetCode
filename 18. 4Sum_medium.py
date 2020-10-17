
# 重点，不要有重复的
# 注意：第二轮循环的关键，要用 s>f+1, 而不是s>0
                # 这样的话，可以允许第一个和第二个elements相同


# 思路: 和3Sum是一样的，但是多加了一层，然后再找twoSum

# 1. 先把nums排序，因为不要重复的，所以这一步必要
# 2. 一共是三个个循环，前两个循环是遍历nums，作为第一二个elements，
# 3. 然后剩下两个element就用2Sum的方法， 可以用hash，可以用指针
# 指针的话left， right，
    # if nums[left]+nums[right]>target: right = right-1
    # if nums[left]+nums[right]<target: left = left+1
    # 直到right == left，就没有答案了

# step 1： sort
# step 2,3 里，如果发现移动之后element是一样的，就一直移动到不一样为止


# TC：O(N^3)
# SC：O(N)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # some edge cases:
        n = len(nums)
        if n < 4:
            return []
        if n == 4 and sum(nums) == target:
            return [nums]

        # first sort nums
        nums.sort()
        ans = []

        # f: index of the first element

        def TwoSum(sub_nums, t):
            left = 0
            m = len(sub_nums)
            right = m - 1
            res = []

            while left < right:
                if left > 0 and sub_nums[left] == sub_nums[left - 1]:
                    left += 1
                    continue
                if sub_nums[left] + sub_nums[right] == t:
                    res.append([sub_nums[left], sub_nums[right]])
                    left += 1
                    right -= 1

                elif sub_nums[left] + sub_nums[right] > t:
                    right -= 1
                elif sub_nums[left] + sub_nums[right] < t:
                    left += 1

            return res

        for f in range(n):
            if f > 0 and nums[f] == nums[f - 1]:
                # skip every lines after this, increase f, until the one which is not ths same as before
                continue
            for s in range(f + 1, n):
                # 注意：这里很关键，要用 s>f+1, 而不是s>0
                # 这样的话，可以允许第一个和第二个elements相同，
                if s > f+1 and nums[s] == nums[s - 1]:
                    continue

                # this will be the new target for TwoSum
                t = target - nums[f] - nums[s]

                # define TwoSum function, return the list eligible elements.
                if len(nums[s + 1:]) >= 2:
                    twoSumlist = TwoSum(nums[s + 1:], t)
                    if twoSumlist:
                        for i in twoSumlist:
                            ans.append([nums[f], nums[s]] + i)
        return ans