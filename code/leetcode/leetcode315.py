class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[]

        for i in range(len(nums)):
            res.append(0)
            for j in range(0,i):
                if nums[j]>nums[i]:
                    res[j]+=1
        return res