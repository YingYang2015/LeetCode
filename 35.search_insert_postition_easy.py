# 35. Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.


# binary search
# define edge cases first
# 指针问题
# ***** 注意： while left <= right!!

# step 1: 两个指针从最两边出发, left, right
# step 2:
# mid = int((left+right)/2)
# compare mid with the target value
# if mid == target, return index = mid
# if mid > target, take the left part, right指针update成mid-1
# if mid < target, take the right part, left 指针update成mid+1
# step 3: repeat step 1,2
# until mid == target, return index = mid
# until left 和right相遇
# return left,
# 因为插进去最后一个比较的时候，一定是比左边大的，而mid等于left这个时候，所以是left

# TC: O(n)
# SC: O(1)

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        n = len(nums)

        if target > nums[n - 1]:
            return n
        if target < nums[0]:
            return 0

        left = 0
        right = n-1
        while left <= right:

            mid = int((left+right) / 2)
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1

            print(left, right)

        return left

s = Solution()

nums = [1,3,5,6]
target = 2

s.searchInsert(nums, target)