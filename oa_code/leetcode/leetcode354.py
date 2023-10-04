import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort()
        dp = [0 for _ in range(len(envelopes))]
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 上面这么写是完全正确的，但是因为dp的二重循环的原因，会超时

        return max(dp)
