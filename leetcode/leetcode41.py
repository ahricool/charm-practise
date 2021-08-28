class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=0
        max_num=1
        min_num=2
        for num in nums:
