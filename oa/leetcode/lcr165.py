class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        dp = [0 for _ in range(len(str(ciphertext)))]
        dp[0] = 1
        for idx in range(1, len(dp)):
            dp[idx] += dp[idx - 1]
            if 9<int(str(ciphertext)[idx - 1:idx + 1]) < 26:
                if idx - 2 >= 0:
                    dp[idx] += dp[idx - 2]
                else:
                    dp[idx] += 1
        return dp[-1]
