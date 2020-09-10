# https://leetcode.com/problems/product-of-array-except-self/solution/

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# Solution is here:
# similar idea as preSum, but create a pre multiplication
# since the division is not allowed to use.
# we can create two pre-multiplication,
    # one from the left to the right
        # first element is 1, and select element is the preSum of the first element in nums
    # one reverse
        # the opposite as before, but the first element is also 1

# TC: O(n)
# SC: (N)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_p = [1 for i in range(n)]
        right_p = [1 for i in range(n)]

        for i in range(n - 1):
            left_p[i + 1] = left_p[i] * nums[i]

        for i in range(n - 1):
            right_p[i + 1] = right_p[i] * nums[n - i - 1]

        right_p = right_p[::-1]
        output = [left_p[i] * right_p[i] for i in range(n)]

        return output

# Now ask for just use O(1) for SC:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_p = 1
        right_p = [1 for i in range(n)]

        for i in range(n - 1):
            right_p[i + 1] = right_p[i] * nums[n - i - 1]

        right_p = right_p[::-1]

        for i in range(n):
            right_p[i] = right_p[i] * left_p
            left_p = left_p * nums[i]

        return right_p