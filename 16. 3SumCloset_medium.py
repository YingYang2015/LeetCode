# 16. 3Sum Closest

# TC: O(N^2)
# SC: O(N), 这是取决于nums.sort()

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 3 layers
        # first layer has the full loop,
        # second and third layer, use two pointers

        n = len(nums)
        if n < 3:
            return []
        if n == 3:
            return sum(nums)

        nums.sort()
        min_diff = float('inf')
        res = target

        for f in range(0, n - 2):
            if f > 0 and nums[f] == nums[f - 1]:
                continue

            s = f + 1
            t = n - 1

            while s < t:
                current_sum = nums[f] + nums[s] + nums[t]
                current_diff = abs(current_sum - target)
                if current_diff < min_diff:
                    min_diff = min(current_diff, min_diff)
                    res = current_sum
                if current_sum < target:
                    s += 1
                else:
                    t -= 1
                if current_diff == 0:
                    return current_sum

        return res
