class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count=[1 for _ in range(len(nums))]
        max_nums=[0 for _ in range(len(nums))]
        count[0]=1
        max_nums[0]=nums[0]
        for i in range(1,len(nums)):
            for j in range(0,i):
                max_nums[0]=
        return max(count)
