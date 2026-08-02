class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Nested for loop, loop thru each possible buy value
    # second loop checks each sell value
    # keep a counter going for profit, if you find a new high profit set equal
    # return difference
    # account for the edge case of not making any transactions, but for this
    # thats just the same as 0 profit so don't need to worry abt i
        profit = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                if prices[sell] - prices[buy] >= profit:
                    profit = prices[sell] - prices[buy]
                else:
                    continue
        return profit

