class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0 for _ in range(amount + 1)]
        for i in range(1,amount + 1):
            res = []
            for c in coins:
                if i - c >= 0 and dp[i - c] >=0:
                    res.append(dp[i - c] + 1)
            dp[i] = min(res) if res else -1
        print(dp)
        return dp[-1]
