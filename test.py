from typing import List
import bisect

# 300
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
# https://leetcode.com/problems/longest-increasing-subsequence/solution/


# 方法二，d就是所求的一个子序列，len就是目前子序列长度，贪心在于这个子序列里的每个值都要尽量小，优化在于替换小值时因为已排序可以用二分查找。
# 考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。
# d[i]
# 无序列表最关键的一句在于： 数组 d[i]表示长度为 i 的最长上升子序列的末尾元素的最小值，即在数组 1,2,3,4,5,6中长度为3的上升子序列可以为 1,2,3也可以为 2,3,4等等但是d[3]=3，即子序列末尾元素最小为3。

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = []

        for i in nums:
            idx = bisect.bisect_left(dp, i)
            if idx == len(dp):
                dp.append(i)
            else:
                dp[idx] = i

        print(dp)
        return len(dp)

s = Solution()
nums = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15 ]
print(s.lengthOfLIS(nums))

