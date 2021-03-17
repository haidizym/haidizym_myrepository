#只要当前利润大于前一天利润，利润就加进去，
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for day in range(len(prices)-1):
            differ = prices[day+1] - prices[day]
            if differ > 0:
                profit += differ
        return profit
