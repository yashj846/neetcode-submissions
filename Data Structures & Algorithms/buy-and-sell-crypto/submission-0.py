class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        max_profit = 0
        for p in range(1, len(prices)):
            sp = prices[p]
            profit = sp - bp
            max_profit = max(profit,max_profit)
            if sp < bp:
                bp = sp
        return(max_profit)
        