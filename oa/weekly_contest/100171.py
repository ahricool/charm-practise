class Solution:
    def incremovableSubarrayCount(self, nums) -> int:

        dp=[0 for _ in range(len(nums))]
        dp[0]=1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]+=dp[j]
        return dp[-1]

print(Solution().incremovableSubarrayCount([1,2,3,4]))
