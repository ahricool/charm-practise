class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0 for _ in range(len(nums))]
        dp[0]=1

        for idx in range(len(nums)):
            if dp[idx]==1:
                for jump in range(1,nums[idx]):
                    if idx+jump<len(nums):
                        dp[idx+jump]=1
        
        return dp[-1]==1
    

# 上面会 ot 因为有2重合循环

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0 for _ in range(len(nums))]
        dp[0]=1
        max_jump=0

        for idx in range(len(nums)):
            if dp[idx]==1 or max_jump>0:
                dp[idx]=1
                max_jump-=1
                max_jump=max(max_jump,nums[idx])

                
        
        return dp[-1]==1
    
# 贪心 不用dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_index=nums[0]
        for idx in range(1,len(nums)):
            if max_index<idx:
                return False
            if max_index>=len(nums)-1:
                return True
            if max_index>=idx:
                max_index=max(max_index,idx+nums[idx])