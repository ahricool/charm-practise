class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for idx in range(len(nums)):
           expect=target-nums[idx]
           if expect in d.keys():
               return [idx,d[expect]]
           else:
               d.update({nums[idx]:idx})

        return 