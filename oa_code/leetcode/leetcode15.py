class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []
        for first in range(len(nums) - 2):
            # 对于连续的数组 直接跳过 不对比了
            if first>0 and nums[first]==nums[first-1]:
                continue


            target = -nums[first]
            second, third = first + 1, len(nums) - 1
            while second < third:
                if second>first+1 and nums[second]==nums[second-1] or nums[second] + nums[third] < target:
                    second+=1

                elif nums[second] + nums[third] == target:
                    phase=[nums[first], nums[second], nums[third]]
                    res.append(phase)
                    second+=1

                elif nums[second] + nums[third] > target:
                    third -= 1
        return res
