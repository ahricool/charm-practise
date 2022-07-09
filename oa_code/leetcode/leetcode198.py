class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0 for _ in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=nums[1]
        dp[2]=nums[0]+nums[2]

        for i in range(3,len(nums)):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i]

        return max(dp)

