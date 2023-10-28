import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx=bisect.bisect_left(nums,target)
        return nums[idx]==target