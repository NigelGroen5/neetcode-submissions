class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for i in range(len(prices)):
            if prices[l] > prices[i]:
                l = i
            elif prices[l] <= prices[i]:
                maxP = max(maxP, prices[i]- prices[l])

        return maxP
            
