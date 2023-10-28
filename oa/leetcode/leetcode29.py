class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=0
        while dividend:
            if divisor&1:
                ans+=1
            dividend>>1
            divisor>>1

        
        return ans