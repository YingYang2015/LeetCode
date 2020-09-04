# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# TC: O(n)
# SC: O(3+n)

class Solution:
    def maxSubArray(self, nums: list) -> int:

        if len(nums) == 0:
            return -1

        new_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            new_sum = max(new_sum + current, current)
            max_sum = max(max_sum, new_sum)

        return max_sum


def maxSubArray_test():
    s = Solution()
    assert s.maxSubArray([0]) == 0
    assert s.maxSubArray([1,2]) == 3
    assert s.maxSubArray([])  == -1

if __name__ == '__main__':
    maxSubArray_test()


# divide and concur
# TC: O(nlogn)
# SC:

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            # print('left', left)
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid + 1, right),
                   self.__max_cross_array(nums, left, mid, right))

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max

s=Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
s.maxSubArray(nums)