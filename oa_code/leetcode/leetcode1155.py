class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        # dp[i][j]=k 投掷i次的和为j的次数为k

        # 初始条件只投一次
        for i in range(1, min(k + 1, target + 1)):
            dp[1][i] = 1

        # 从两次开始
        for i in range(2, len(dp)):
            for j in range(1, len(dp[0])):
                for roll in range(1, k + 1):
                    if j - roll > 0:
                        dp[i][j] += dp[i - 1][j - roll]

        res = dp[-1][-1]

        return int(res % (10 ** 9 + 7))


