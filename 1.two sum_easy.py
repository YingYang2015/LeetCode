# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# TC:O(N)


# One pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = collections.defaultdict(list)

        # step 1: get a dictionary with key = i of nums, value = target-i
        # step 2: for each key, check if the value is in nums, if so, return two index

        for i, val in enumerate(nums):
            if target - val in dict.keys():
                return [i, dict[target - val]]
            else:
                dict[val] = i