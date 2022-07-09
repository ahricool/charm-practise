class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target=nums[0]
        count=1
        for idx in range(1,len(nums)):
            if target==nums[idx]:
                count+=1
            else:
                count-=1
                if count==0:
                    target=nums[idx]
                    count=1

        return target