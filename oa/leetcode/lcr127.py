class Solution:
    def trainWays(self, num: int) -> int:
        if num==0:
            return 1

        if num==1:
            return 1

        dp=[0 for i in range(num)]
        dp[0],dp[1]=1,2
        for idx in range(2,len(dp)):
            dp[idx]=dp[idx-1]+dp[idx-2]

        return dp[-1]%1000000007