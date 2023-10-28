class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if len(nums)<2 or s%2!=0:
            return False

        t=s//2

        # dp[i][j] 表示(0,i)是否存在 子数组和 为j
        dp=[[0 for _ in range(t+1)] for _ in range(len(nums))]

        # 初始条件
        for idx in range(len(nums)):
            dp[idx][nums[idx]]=1
            dp[idx][0]=1




        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j-nums[i]>=0:
                    dp[i][j]=dp[i][j-nums[i]] or dp[i][j] or dp[i][j-1]

        return bool(dp[-1][-1])




