class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def _find(nums,l,r,target):
            while l <= r:
                idx=(l+r)//2
                if nums[idx]==target:
                    return idx
                elif nums[idx]<target:
                    l=idx+1
                else:
                    r=idx-1
            return -1
        
        idx=_find(nums,0,len(nums)-1,target)
        if idx==-1:
            return [-1,-1]
        else:
            l=idx
            while l>=0 and nums[l]==target:
                l-=1
            r=idx
            while r<=len(nums)-1 and nums[r]==target:
                r+=1
            return [l+1,r-1]
        