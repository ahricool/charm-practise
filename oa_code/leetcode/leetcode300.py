# 之前简直胡乱写一通，不知道在想什么
# 2012，12,11 随便几行代码，轻松秒杀

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i]=dp[j]+1
        return max(dp)
