class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0]=="0":
            return 0

        dp=[0 for _ in range(len(s))]
        dp[0]=1

        for idx in range(1,len(dp)):
            if s[idx]!="0":
                dp[idx]+=dp[idx-1]
            if idx-2>=0 and int(s[idx-1:idx+1])<=26:
                dp[idx]+=dp[idx-2]

        return dp[-1]



