class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        # 所有的单调递增区间累计即可
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                ans+=prices[i+1]-prices[i]

        return ans
                
