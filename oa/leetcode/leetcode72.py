

# 编辑距离算法是一个非常重要的算法，用来评价两个字符串（数据）的相似度。
# 在机器翻译，语音识别有非常广泛的应用。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word2)+1,len(word1)+1
        dp=[[0 for _ in range(n)] for _ in range(m)]   
        dp[0][0]=0
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+1
        for j in range(1,n):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, m):
            for j in range(1, n):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

        return dp[m - 1][n - 1]

