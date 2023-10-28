class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]!=val:
                l+=1
                continue
            if nums[l]==val and nums[r]==val:
                r-=1
                continue
            if nums[l]==val and nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return l