class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            # if price at right pointer is less, l = r
            if prices[r] < prices[l]:
                l = r
            elif prices[r] >= prices[l]:
                max_profit = max(max_profit, prices[r]-prices[l])
        return max_profit
            
            # if right > less, update max profit, keep going

            # if right = less, doesn't matter



# 