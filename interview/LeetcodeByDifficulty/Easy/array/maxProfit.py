class Solution:
    def maxProfit(self, prices):
        """ return max profit in int""" 
        bought = prices[0]
        profit = 0
        for p in prices:
            if p > bought:
                profit += p - bought
            bought = p
        return profit