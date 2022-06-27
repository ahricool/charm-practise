import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            mid=(l+r)//2
            res = min(res, nums[mid])
            if nums[mid]>nums[l]: # 左边是升序 右边未知
                res = min(res, nums[l])
                l=mid+1
                continue
            elif nums[mid]<nums[l]: # 右边是升序 左边未知
                r=mid-1
                continue

            elif nums[mid]==nums[l]: # 无法判断 但是也能缩小范围
                l=l+1
                continue

        return res








