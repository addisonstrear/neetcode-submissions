class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find the best sell point, then the best buy point before that
        buy = prices[0]
        best = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            if sell - buy > best:
                best = sell - buy
            if prices[i] < buy:
                buy = prices[i]

    
        if best < 0:
            return 0
        return best

        