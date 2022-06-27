class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow,fast=0,0 # 滑动窗口
        current_sum=nums[0]
        min_len=len(nums)+1
        while fast<len(nums):
            if current_sum>=target:
                min_len=min(min_len,fast-slow+1)
                current_sum = current_sum - nums[slow]
                slow+=1
            else:
                fast += 1
                if fast<len(nums):
                    current_sum=current_sum+nums[fast]

        if min_len==len(nums)+1:
            return 0
        else:

            return min_len