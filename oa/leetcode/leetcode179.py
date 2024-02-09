class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=lambda x: x * 10, reverse=True)
        return "".join(nums).lstrip("0") or "0"