class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<2:
            return 0
        dp = [0 for _ in range(len(s))]
        if s[0] == "(" and s[1] == ")":
            dp[1] = 2
        else:
            dp[1] = 0

        for i in range(2, len(s)):
            if s[i] == "(":
                dp[i] = 0
            else:
                if dp[i-1]>0 and i - dp[i - 1] - 1>=0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2
                    if i-dp[i]>=0:
                        dp[i] += dp[i-dp[i]]
                    continue
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                    continue
        return max(dp)
