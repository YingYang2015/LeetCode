# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/


#1. Brutal Force
# Idea is to simply calculate the profit corresponding to all
# the possible sets of transactions and find out the maximum profit out of them.
# Time complexity: O(N^n)
# Space complexity: O(n)


# 2. Approach 2: Peak Valley Approach
# The key point is we need to consider every peak immediately
# following a valley to maximize the profit.
# In case we skip one of the peaks (trying to obtain more profit),
# we will end up losing the profit over one of the transactions
# leading to an overall lesser profit.
# Time complexity: O(n^2)
# Space complexity: O(1)


# Approach 3: add all positive profit
# Time complexity: O(n)
# Space complexity: O(1)
# Here is the point, when you think about it in terms of math,
# day 4 - day 1 = day 4 - day 3 + day 3 - day 2 + day 2 - day 1,
# notice all the inner cancellations? that's a clever way to calculate,
# and is easily applied in a for loop, so in approach 3 we have the
# code: maxprofit += prices[i] - prices[i - 1]. So in short,
# it's just a clever way to achieve the same effect,
# which doesn't mean you have to buy on day 1 & sell on day 2,
# buy on day 2 & sell on day 3, etc. Hope this helps!


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
        max_profit = 0
        for i in range(n-1):
            max_profit = max_profit+ max(prices[i+1] - prices[i], 0)

        return max_profit



# 2. Approach 2: Peak Valley Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0

        valley = prices[0]
        peak = prices[0]
        max_profit = 0

        i = 0
        while i < (n-1):
            while i<(n-1) and (prices[i+1]<prices[i]):
                i+=1
            valley = prices[i]
            while i<(n-1) and (prices[i]<prices[i+1]):
                i+=1
            peak = prices[i]

            max_profit = max_profit + peak-valley

        return max_profit



# Brutal Force sample code: Java


# class Solution {
#     public int maxProfit(int[] prices) {
#         return calculate(prices, 0);
#     }
#
#     public int calculate(int prices[], int s) {
#         if (s >= prices.length)
#             return 0;
#         int max = 0;
#         for (int start = s; start < prices.length; start++) {
#             int maxprofit = 0;
#             for (int i = start + 1; i < prices.length; i++) {
#                 if (prices[start] < prices[i]) {
#                     int profit = calculate(prices, i + 1) + prices[i] - prices[start];
#                     if (profit > maxprofit)
#                         maxprofit = profit;
#                 }
#             }
#             if (maxprofit > max)
#                 max = maxprofit;
#         }
#         return max;
#     }
# }