class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        max_profit = 0
        while rp < len(prices):
            profit = prices[rp] - prices[lp]
            if profit <= 0:
                lp = rp
            max_profit = max(max_profit, profit)
            rp += 1
        return max_profit