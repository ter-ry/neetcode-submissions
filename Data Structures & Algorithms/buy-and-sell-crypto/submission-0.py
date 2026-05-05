class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            if i > buy:
                sell = i
                profit = max((sell-buy), profit)
            elif i < buy:
                buy = i
            
        return profit

        