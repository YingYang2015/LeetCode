# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#

# Note:三种方法，
# 1. 直接sort,去掉0
# 2. recursion， recursion不好做
# 3. 指针，
# 指针的话，要注意 这个情况 "if nums1[p1] < nums2[p2]:"， 变成0时要handel (if p1 < m + p2:)
# 指针方法就是从左到右，然后插入，update p1, p2

# TC: O(N)
# SC: O(N)
# 3. 指针
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0

        while p2 < n and p1 < m+n:
            if nums1[p1] < nums2[p2]:
                if p1 < m + p2:
                    p1 += 1
                else:
                    nums1[p1] = nums2[p2]
                    p2 += 1
                    p1 += 1
            elif nums1[p1] >= nums2[p2]:
                nums1[p1 + 1:] = nums1[p1:-1]
                nums1[p1] = nums2[p2]
                p2 += 1
                p1 += 1
        return nums1

nums1 = [2,0]
m=1
nums2 = [1]
n=1

s = Solution()
print(s.merge(nums1, m, nums2, n))


# method 2: recursion
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         def helper(o, i, j):
#             if i < m and (j >= n or nums1[i] <= nums2[j]):
#                 helper(o + 1, i + 1, j)
#                 nums1[o] = nums1[i]
#             elif j < n:
#                 helper(o + 1, i, j + 1)
#                 nums1[o] = nums2[j]
#
#         helper(0, 0, 0)
