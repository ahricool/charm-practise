# 这个题的难度是有两个dp数组  要分别想清楚两个数组的定义是什么

class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp = [1 for _ in range(len(nums))]  # 在此位置结尾的最长递增子序列的长度
        count = [1 for _ in range(len(nums))]  # 在此位置结尾的最长递增子序列的个数
        for i in range(1, len(nums)):
            for pre in range(i):
                if nums[pre] < nums[i]:
                    if dp[pre] + 1 > dp[i]:  # 发现更长的最长子序列
                        dp[i] = dp[pre] + 1
                        count[i] =count[pre]
                    elif dp[pre] +1 ==dp[i]:  # 发现同长度的最长子序列
                        count[i]=count[pre]+count[i]



        max_count=0
        for index in range(len(dp)):
            if dp[index]==max(dp):
                max_count+=count[index]


        return max_count