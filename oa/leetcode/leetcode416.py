class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if len(nums) < 2 or s % 2 != 0:
            return False

        t = s // 2

        # dp[i][j] 表示(0,i)是否存在 子数组和 为j
        dp = [[False for _ in range(t + 1)] for _ in range(len(nums))]

        # 初始条件
        # 肯定存在从(0,idx) 上和为0的子序列
        for idx in range(len(nums)):
            dp[idx][0] = True

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                # 不选择这个数 dp[i][j]=dp[i-1][j]
                if i >= 1:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                # 选择这个数
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i]]

        return bool(dp[-1][-1])




