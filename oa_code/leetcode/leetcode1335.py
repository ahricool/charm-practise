import math
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        dp=[[0 for _ in range(len(jobDifficulty))] for _ in range(d)]

        for idx in range(len(dp[0])):
            dp[0][idx]=max(jobDifficulty[0:idx+1])

        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if i>j:
                    continue
                min_diff=math.inf
                for k in range(0,j):
                    if dp[i-1][k]==0:
                        continue
                    min_diff=min(min_diff,dp[i-1][k]+max(jobDifficulty[k+1:j+1]))
                dp[i][j]=min_diff



        return dp[-1][-1]
