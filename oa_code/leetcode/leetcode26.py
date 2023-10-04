class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow,fast=1,1
        cur=nums[0]
        while fast<len(nums):
            if nums[fast]==cur:
                fast+=1
            else:
                cur=nums[slow]=nums[fast]
                slow+=1
                fast+=1
        nums=nums[0:slow]
        return nums
                
