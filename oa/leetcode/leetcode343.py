class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0 for _ in range(n)]

        for i in range(n):
            max_volume=0
            for j in range(0,i):
                volume=dp[j]*(i-j)
                if max_volume<volume:
                    max_volume=volume
            if i!=n-1:
                dp[i]=max(i+1,max_volume)
            else:
                dp[i]=max_volume

        return max(dp)

