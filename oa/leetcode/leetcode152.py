
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp=[None for _ in range(len(nums))]
        min_dp=[None for _ in range(len(nums))]

        max_dp[0]=min_dp[0]=nums[0]

        for i in range(1,len(nums)):
            max_dp[i]=max(max_dp[i-1]*nums[i],min_dp[i-1]*nums[i],nums[i])
            min_dp[i]=min(max_dp[i-1]*nums[i],min_dp[i-1]*nums[i],nums[i])

        return max(max_dp)
