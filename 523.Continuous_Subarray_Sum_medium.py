# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

#https://leetcode.com/problems/subarray-sum-equals-k/solution/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Solution 1: preSum, then遍历
# TC: O(n^2)
# SC: O(n)

# Solution 2: start from left, calcualte sum when right moves to the end, count when sum = k
# then move left to n as well
# TC: O(n^2)
# SC: O(1)

# Solution 3: Hashmap: look at the graph in solution (最优化的）
# TC: O(n)
# SC: O(1)

# Solution 3:
# Insight for solution 3 seems so simple, after you get.
# If two number have the same remainder from division by a number then they differ by a multiple of that divisor.
# if x%k == y%k then (x-y) must be multiple of k. (x-y)%k =0.



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapping = {0: -1}
        prefix = 0
        for i in range(len(nums)):

            prefix = prefix + nums[i]

            # 这里count了k = 0 的情况
            key = prefix % k if k else prefix

            # 注意：这里已经garantee key一直维持最小的index了

            if key not in mapping:
                mapping[key] = i
            elif i - mapping[key] > 1:
                return True

        return False


# Solution 1: preSum, then遍历
# 遍历的时候要考虑k= 0的情况，k= 0的话，就是 if (summ == k || (k != 0 && summ % k == 0))

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> int:
        # Solution 1: use preSum,
        # then loop both for  from left to right, use preSum[right] - preSum[left],
        # calcuate the sum == k or summ%k = 0, and right-left>=2 then count +=1
        n = len(nums)
        if n == 0:
            return 0

        preSum = [0 for i in range(n + 1)]
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        count_k = 0
        for left in range(n):
            for right in range(left + 1, n + 1):
                summ = preSum[right] - preSum[left]
                if summ == k or (k != 0 and summ % k == 0):
                    if right-left>=2:
                        count_k += 1

        return count_k