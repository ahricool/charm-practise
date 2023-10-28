class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i*j==0:
                    dp[i][j]=matrix[i][j]
                else:
                    if dp[i-1][j]

