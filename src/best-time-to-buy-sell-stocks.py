class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n, profit = len(prices), 0

        # divide array into two part
        # [0, i)
        # [i, n)

        for i in range(n):
            # calculate the left profit
            # then the right profit
            # combine then
            leftProfit = self.get_profit(0, i, prices)
            rightProfit = self.get_profit(i, n, prices)
            profit = max(profit, leftProfit + rightProfit)

        return profit

    def get_profit(self, lbound, rbound, prices):
        minSellVal, profit = float("inf"), 0
        for i in range(lbound, rbound):
            minSellVal = min(minSellVal, prices[i])
            profit = max(profit, prices[i]-minSellVal)
        return profit
