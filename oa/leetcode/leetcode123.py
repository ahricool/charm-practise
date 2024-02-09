class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1=b2=-prices[0]
        s1=s2=0
        for i in range(1,len(prices)):
            b1=max(b1,-prices[i])
            s1=max(s1,b1+prices[i])
            b2=max(b2,b2-prices[i])
            s2=max(s2,b2+prices[i])

        return s2