class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        ans=nums[0]+nums[1]+nums[2]

        for idx in range(len(nums)-2):
            l,r=idx+1,len(nums)
            while l<r:
                s = nums[idx] + nums[l] + nums[r]
                if abs(s-target)<abs(ans-target):
                    ans=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return 0

        return ans





