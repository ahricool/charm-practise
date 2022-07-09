
# 转移方程 dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0]=int(matrix[i][0])
        for j in range(n):
            dp[0][j]=int(matrix[0][j])

        for i in range(1,m):
            for j in range(1,n):
                if int(matrix[i][j])==0:
                    dp[i][j]=0
                else:
                    expect=min([dp[i-1][j],dp[i][j-1],dp[i-1][j-1]])
                    dp[i][j]=expect+1
        max_side=max([ max(i) for i in dp])
        return max_side**2



