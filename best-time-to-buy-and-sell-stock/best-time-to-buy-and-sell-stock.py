class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        
        buy = prices[0]
        sell = 0
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = 0
            else:
                if prices[i] > sell:
                    sell = prices[i]
                    
                    profit = sell - buy
                    if profit > maxprofit:
                        maxprofit = profit
        
        return maxprofit
                
        