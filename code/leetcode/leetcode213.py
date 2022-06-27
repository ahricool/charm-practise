class Solution:

    def rob(self, nums: List[int]) -> int:
        # 通过两次的dp 把所有可能的结果覆盖
        # 把问题拆分，然后分两次dp解决

        if len(nums)<=3:
            return max(nums)

        def rob_range(start,end):
            dp=[0 for _ in range(end-start+1)]
            dp[0]=nums[start]
            dp[1]=max(nums[start],nums[start+1])

            for idx in range(2,len(dp)):

                dp[idx]=max(dp[idx-1],dp[idx-2]+nums[start+idx])


            return dp[-1]

        return max(rob_range(0,len(nums)-2),rob_range(1,len(nums)-1))