class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        point=(l+r)/2

        if nums[point]>nums[r]:
