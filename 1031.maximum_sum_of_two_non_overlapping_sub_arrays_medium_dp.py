

### NOTE: 此题不能先找local maximum，
# 1.我第一次的方法是先找best L, 再找best M， 再反过来找一遍，比较两个sum的大小
# 但是这样就不对了，
# 2.应该对每一个possible 的L list，来找前面或者后面的最大的M list !!
#   We can use prefix sums to calculate any subarray sum quickly.
#   For each L length subarray,
#   find the best possible M length subarray that occurs before and after it.
# 2.1 太慢了，跑不过，算了太多次的 rolling window的 pre和post的max sum O(2N^2)
# 2.2 优化了一下，把算好的先存起来，memo，rolling window就只算一次
# DP: O(n)
# Step 1: get the presum, prefix sum
# Step 2: there are two cases:
#         1. L on the left, and M on the right
#         2. M on the left, and L on the right
# Step 3: compare the two, and pic the bigger one
#    base status: is the L+M from the left
#    status change function: Based on step 2

from typing import List


class Solution():
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        #preSum = A.copy()
        # preSum[0] = A[0]
        preSum = [0 for i in range(n+1)]
        # for i in range(1, n):
        for i in range(1, n+1):
            preSum[i] = A[i-1] + preSum[i - 1]

        # define base status
        res = preSum[L + M - 1]
        Lmax = preSum[L - 1]
        Mmax = preSum[M - 1]

        for i in range(L + M, n+1):
            Lmax = max(Lmax, preSum[i - M] - preSum[i - M - L])
            Mmax = max(Mmax, preSum[i - L] - preSum[i - M - L])
            res = max(res, Lmax + preSum[i] - preSum[i - M],
                      Mmax + preSum[i] - preSum[i - L])
        return res


# version 1:
from typing import List
# 2.1
# class Solution:
#     def maxSubarray(self, nums: List[int], n: int):
#
#         if len(nums) < n:
#             return 0
#         max_sum = 0
#
#         for i in range(0, len(nums)):
#             current_array = nums[i:i+n]
#             current_sum = sum(nums[i:i+n])
#             max_sum = max(current_sum, max_sum)
#         return max_sum

    # def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
    #
    #     # step 1: define a function which can return maximum sub array and index and sum
    #     max_sum = 0
    #     for i in range(0, len(A)):
    #         current_array = A[i:i+L]
    #         pre_L = A[0:i]
    #         post_L = A[(i+L):]
    #
    #         M_sum_pre  = self.maxSubarray(pre_L, M)
    #         M_sum_post = self.maxSubarray(post_L, M)
    #         new_sum = sum(current_array) + max(M_sum_pre, M_sum_post)
    #         max_sum = max(max_sum, new_sum)
    #
    #     return max_sum
# method 3
# class Solution:
#     def maxSubarray(self, nums: List[int], n: int):
#
#         if len(nums) < n:
#             return 0
#         max_sum = 0
#
#         for i in range(0, len(nums)):
#             current_array = nums[i:i+n]
#             current_sum = sum(nums[i:i+n])
#             max_sum = max(current_sum, max_sum)
#         return max_sum
#
#
#     def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
#
#         # step 1: define a function which can return maximum sub array and index and sum
#         max_sum = 0
#         n = len(A)
#         M_max_sum_pre = [0 for i in range(M)]
#         M_max_sum_post = []
#         for i in range(0, n-M-L+1):
#             M_max_sum_pre.append(self.maxSubarray(A[0:i+M], M))
#             M_max_sum_post.append(self.maxSubarray(A[i+L:], M))
#
#         M_max_sum_post=M_max_sum_post + [0 for i in range(M)]
#
#         print(len(M_max_sum_pre))
#         print(len(M_max_sum_post))
#         for i in range(0, n-L+1):
#             current_array = A[i:i+L]
#             print(i)
#             new_sum = sum(current_array) + max(M_max_sum_pre[i], M_max_sum_post[i])
#
#             max_sum = max(max_sum, new_sum)
#
#         return max_sum
# 355914
A = [519,990,122,978,979,715,10,332,1000,70,888,295,770,672,508,845,701,406,781,398,750,574,84,842,839,41,600,554,197,869,904,456,36,747,450,640,930,626,567,242,822,386,799,709,190,446,347,659,221,788,48,678,590,547,210,796,252,974,933,12,394,716,166,781,770,919,517,884,898,56,695,452,954,292,797,104,644,916,57,140,12,319,910,300,153,384,861,606,369,519,313,500,18,184,700,475,458,230,802,10,296,967,327,9,780,54,969,865,512,37,563,730,183,509,152,361,66,387,353,190,691,183,371,372,485,362,761,993,125,196,143,339,139,110,188,598,723,272,840,353,532,232,158,851,836,922,644,391,199,978,977,165,58,934,929,604,493,717,277,112,617,595,86,828,137,936,910,260,126,897,644,32,895,915,331,905,23,0,647,138,513,123,509,272,961,493,181,71,797,952,217,778,358,522,14,228,624,147,690,597,812,517,468,208,384,312,654,260,593,406,554,865,922,740,233,217,963,809,48,806,492,399,727,20,462,15,704,820,744,467,734,871,28,422,334,988,511,497,137,456,987,233,425,887,152,838,390,741,810,867,892,680,165,829,397,385,730,787,497,977,374,462,121,966,236,631,937,699,348,510,807,92,878,908,859,470,831,123,108,56,867,857,171,456,211,160,924,882,621,10,345,465,908,48,804,143,928,720,82,555,107,179,943,15,512,319,941,26,719,332,782,364,583,832,48,505,414,325,995,969,312,630,904,677,762,261,566,595,542,218,949,422,392,654,934,429,564,508,175,409,47,753,537,601,192,257,597,173,566,290,958,810,640,314,842,23,379,955,735,600,947,927,127,657,794,253,378,709,300,757,672,68,828,423,575,302,861,981,683,222,104,162,261,977,510,38,454,715,238,249,622,308,321,852,616,41,734,19,473,796,506,497,856,245,211,561,826,459,50,855,737,844,971,278,686,598,25,796,280,429,80,376,416,867,503,522,482,517,895,428,617,232,890,1,694,411,426,16,855,424,644,770,47,352,606,369,90,491,6,521,239,349,189,34,627,376,24,528,925,381,125,887,296,105,89,189,749,821,798,543,767,825,472,517,381,803,497,752,750,865,893,843,919,897,601,527,753,65,990,535,253,161,619,81,975,582,591,458,281,640,352,802,454,491,646,163,562,242,819,931,852,512,785,641,819,286,804,785,797,596,791,690,110,447,175,688,118,931,878,811,485,685,128,194,551,724,889,986,168,294,139,446,266,660,874,665,395,847,305,764,994,651,16,235,269,692,38,90,876,458,836,322,119,401,842,355,111,230,46,365,755,856,347,753,316,324,359,608,949,282,408,299,291,961,689,438,747,936,211,834,314,436,134,413,804,349,820,114,283,781,714,383,971,820,899,18,247,278,259,816,308,712,709,231,198,244,718,450,763,292,32,321,318,435,205,293,593,488,245,159,222,446,372,845,338,708,705,135,908,200,893,673,311,379,729,575,679,885,485,336,310,688,61,186,469,256,855,547,589,918,533,207,786,394,647,696,834,564,965,289,442,166,61,363,251,764,199,357,240,379,615,876,42,656,434,507,756,450,225,882,574,650,803,551,312,299,932,187,417,351,214,511,741,996,440,759,485,799,356,783,18,501,460,24,349,101,371,533,591,179,15,387,971,731,617,438,509,916,367,218,751,920,693,731,932,496,326,752,636,88,337,873,776,60,404,353,271,257,562,726,230,868,623,301,96,34,65,340,335,528,975,876,589,58,46,363,403,903,314,671,323,582,396,529,392,734,528,440,115,851,282,600,461,400,258,488,551,135,269,694,175,183,382,118,837,162,737,993,146,331,328,438,67,618,741,974,421,662,436,167,278,886,52,871,758,521,921,532,513,222,466,819,16,437,707,667,3,494,484,261,831,996,425,577,3,555,542,831,274,104,66,927,464,755,668,495,962,342,104,428,980,710,461,479,55,487,97,377,163,31,822,516,440,667,269,932,961,796,67,758,613,617,322,113,658,902,141,456,821,455,659,726,112,490,878,985,904,472,301,905,396,155,544,868,430,203,299,305,632,368,130,470,505,11,150,898,108,620,474,405,734,674,127,384,943,670,646,853,356,98,666,380,531,713,987,320,603,95,781,122,970,888,314,638,430,957,972,578,695,218,86,573,222,937,387,304,580,752,227,199,69,642,689,916,665,690,277,154,273,697,983,187,268,406,835,730,156,691,779,348,768,148,494,309,891,64,226,331,514,609,554,782,499,662,731,392,384,486,265,489,327,318,300,902,609,606,593,282,365,741]
L = 673

M = 22

s = Solution()
print(s.maxSumTwoNoOverlap(A, L, M))