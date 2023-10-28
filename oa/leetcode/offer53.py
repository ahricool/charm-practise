class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        others=[]
        for idx in range(len(nums)):
            if abs(nums[idx])==len(nums):
                others.append(abs(nums[idx]))
                continue
            if nums[abs(nums[idx])]==0:
                others.append(abs(nums[idx]))
                continue
            nums[abs(nums[idx])]=-nums[abs(nums[idx])]

        for idx in range(len(nums)):
            if nums[idx]>=0 and  idx not in others:
                return idx

        return len(nums)

