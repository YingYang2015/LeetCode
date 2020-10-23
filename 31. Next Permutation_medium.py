# 31. Next Permutation

# 解题思路：
# 双指针
# 指针[p1]从最后还是走，如果这个数比前面的大，什么都不用做,p1往前走
# if nums[p1] <= nums[p1-1]: p1 -= 1
# if nums[p1] > nums[p1-1]:
# 需要把nums[p1-1]换了
# 引入p2, 还是从后面开始，找到第一个大于p1-1的值，呼唤
# 再把p1-1后面的数据排序 —————— 注意不要忘了

# TC: O(N): In worst case, only two scans of the whole array are needed.
# SC: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(l, a, b):
            sv = nums[a]
            nums[a] = nums[b]
            nums[b] = sv

        n = len(nums)
        if n <= 1:
            return nums
        p1 = n - 1
        p2 = n - 1
        while p1 > 0:
            if nums[p1] > nums[p1 - 1]:
                while p2 > 0:
                    if nums[p1 - 1] < nums[p2]:
                        swap(nums, p1 - 1, p2)
                        nums[p1:] = sorted(nums[p1:])
                        return nums
                    p2 -= 1
            p1 -= 1

        if p2 == n - 1:
            return nums.sort()

