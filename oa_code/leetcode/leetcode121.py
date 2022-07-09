class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_revenue=0
        min_price=prices[0]
        for p in prices:
            if min_price>p:
                min_price=p
            elif p-min_price>max_revenue:
                max_revenue=p-min_price
        return max_revenue

