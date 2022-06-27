

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        import math
        max_list=sorted(nums[0:3])
        min_list=sorted(nums[0:2])

        for i in nums:


