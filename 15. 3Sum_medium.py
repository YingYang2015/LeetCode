# 15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.

# 重点，不要有重复的

# 思路：
# 1. 先把nums排序，因为不要重复的，所以这一步必要
# 2. 一共是两个循环，第一个循环是遍历nums，作为第一个element，
# 3. 然后剩下两个element就用2Sum的方法， 可以用hash，可以用指针
# 指针的话left， right，
    # if nums[left]+nums[right]>target: right = right-1
    # if nums[left]+nums[right]<target: left = left+1
    # 直到right == left，就没有答案了

# step 1： sort
# step 2,3 里，如果发现移动之后element是一样的，就一直移动到不一样为止



from typing import List

class Solution():
    def ThreeSum(self, nums: List[int], k: int) -> List[List[int]]:
        # some edge cases:
        n = len(nums)
        if n < 3:
            return []
        if n == 3 and sum(nums) == k:
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
                if left>0 and sub_nums[left] == sub_nums[left-1]:
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
            if f>0 and nums[f] == nums[f-1]:
                # skip every lines after this, increase f, until the one which is not ths same as before
                continue
            # this will be the new target for TwoSum
            t = k - nums[f]
            # print(f, nums[f])
            # define TwoSum function, return the list eligible elements.
            if len(nums[f+1:])>=2:
                twoSumlist = TwoSum(nums[f+1:], t)
                if twoSumlist:
                    for i in twoSumlist:
                        ans.append([nums[f]]+i)
        return ans

s = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
#ums = [-2, 0, 0, 1]
k = 0

print(s.ThreeSum(nums, k))






