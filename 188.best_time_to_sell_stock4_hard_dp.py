# you can buy k times


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# TC: O(n*k)
# SC: O(n*k)

# use dynamic programing

# Step 1: base case
    # 1. 第一天结束，还没有交易：d0[0][0] = 0
    # 2. 第一天结束，买了股票： d1[0][0] = -prices[0]
    # 3. 一直没有交易过:
        # 3.1:          一直没有买过：d0[i][0] = 0
        # 3.2: 买了一次，一直没有卖过：d1[i][0] = max(-prices[i], d1[i-1][0])
    # 4.第一天，不管j等于几，都应该给-price
#          for j in range(k+1):
#             d1[0][j] = -prices[0]

# Step 2：定义状态, 手上的profit
    # 1. 第i天结束，交易完后：手里有股票，已经交易了 j 次： d1[i][j]
    # 2. 第i天结束，交易完后：手里没有股票 ，已经交易了 j 次: d0[i][j]
# Step 3：update状态
    # 每一次update两个选择：保持不变，买(d1)或者卖(d0)
    # d1[i][j] = max(d1[i-1][j], d0[i-1][j] -prices[i])
    # d0[i][j] = max(d0[i-1][j], d1[i-1][j-1]+ prices[i])
# Step 4: 确认return result, 交易n次
    # result = d0[n-1][k]





class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0
        if k > n/2:
            profit = 0
            # this means buy and sell unlimited times
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i - 1])
            return profit

        d0 = [[0 for i in range(k + 1)] for i in range(n)]
        d1 = [[0 for i in range(k + 1)] for i in range(n)]

        # define base cases
        d0[0][0] = 0
        for j in range(k+1):
            d1[0][j] = -prices[0]
        for i in range(1, n):
            d0[i][0] = 0
            d1[i][0] = max(-prices[i], d1[i - 1][0])

        # update status
        for i in range(1, n):
            for j in range(1, k + 1):
                d1[i][j] = max(d1[i - 1][j], d0[i - 1][j] - prices[i])
                d0[i][j] = max(d0[i - 1][j], d1[i - 1][j - 1] + prices[i])

        return d0[n - 1][k]

s = Solution()
prices = [1,2,4,2,5,7,2,4,9,0]
k  = 4
print(s.maxProfit(k,prices))


