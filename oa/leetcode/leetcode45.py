import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[ math.inf for _ in range(len( nums))]
        for index in range(len(nums)):
            for j in range(1,nums[index]+1):
                if index+j<len(nums):
                    dp[index+j]=min(dp[index]+1,dp[index+j])
                    print(dp)
        return dp[-1]
