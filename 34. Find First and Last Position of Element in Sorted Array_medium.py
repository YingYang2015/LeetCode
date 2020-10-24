# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].


# Solution:
# Step 1: use binary search to find the any index which equals to target
# Step 2: goes left and right of this index, find the left most and right most

# TC: O(logN + N)
# SC: O(1)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def binary_search(nums, target):

            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1

            return l

        # return一个ind，可能是满足target的人任意坐标
        ind = binary_search(nums, target)

        # 这是target比所有值都大的情况
        if ind >= len(nums):
            return [-1, -1]
        #  这是target在中间，但是不存在的情况，可以插入在这
        if nums[ind] != target:
            return [-1, -1]

        l = ind
        r = ind

        while l >= 0:
            if nums[l] == target:
                l -= 1
            else:
                break

        while r < len(nums):
            if nums[r] == target:
                r += 1
            else:
                break

        return [l + 1, r - 1]
