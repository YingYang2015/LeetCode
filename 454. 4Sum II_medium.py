# 454. 4Sum II

# 解题思路：
# 每两个相加
# 头两个相加的时候用Hash map保存起来
# 第二次的话到hashmap里找-total

# TC： O（N^2）
# SC：O（N^2）
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        # Brutal Force:
        # 4 loops, A provides the 1st element, B -> 2nd element, C-> 3rd, D -> 4th

        n = len(A)
        if n == 0:
            return 0

        dict = collections.defaultdict(int)

        res = 0
        for l1 in range(n):
            for l2 in range(n):
                total = A[l1] + B[l2]
                dict[total] += 1

        for l3 in range(n):
            for l4 in range(n):
                total = C[l3] + D[l4]
                res += dict[-total]

        return res