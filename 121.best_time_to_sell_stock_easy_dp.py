
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.

# TC: O(n): only one single pass is needed
# SC: O(1): only fur variables are needed, can be reduced to 2

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n <= 1:
            return 0

        profit = 0
        min_price = prices[0]

        for i in range(1 ,n):
            current_price = prices[i]
            new_profit = current_price - min_price
            profit = max(profit, new_profit)
            min_price = min(min_price, current_price)

        return profit

def maxProfit_test():
    s = Solution()
    assert s.maxProfit([0,0]) == 0
    assert s.maxProfit([0]) == 0
    assert s.maxProfit([5,4,3,2,1]) == 0
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4

if __name__ == '__main__':
    maxProfit_test()