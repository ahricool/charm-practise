class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0 for _ in range(amount+1)]
        dp[0]=1
        for c in coins:
            for idx in range(1,len(dp)):
                if idx-c>=0:
                    dp[idx]+=dp[idx-c]


        return dp[-1]
