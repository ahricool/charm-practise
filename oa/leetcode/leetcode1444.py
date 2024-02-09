class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        dp=[[0 for i in range(len(pizza))] for _ in range(2)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):


                