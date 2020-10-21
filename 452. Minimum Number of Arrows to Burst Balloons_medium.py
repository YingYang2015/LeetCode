# 452. Minimum Number of Arrows to Burst Balloons

# 最少数arrow射气球
# 气球坐标：points = [[10,16],[2,8],[1,6],[7,12]]
# Example：
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

# 解题思路：
# 按照每个气球的x_end排序
# 两个指针：b_l是第一个气球，b_r开始往右移动看气球
# 如果 b_r[start] <= b_l[end], 同一个arrow可以射中两个，继续向右移动b_r
# 直到 b_r[start] > b_l[end], 需要增加一个arrow，把b_l变成b_r，b_r+=1
# TC：O(NlogN): 是排序的速度
# SC：O(1)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n

        points.sort(key=lambda x: x[1])
        res = 1
        b_r = 0
        b_l = 0

        while b_r < n and b_l < n:
            if points[b_r][0] <= points[b_l][1]:
                b_r += 1
            else:
                b_l = b_r
                b_r += 1
                res += 1
        return res