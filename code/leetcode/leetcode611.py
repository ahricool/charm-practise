class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for first in range(len(nums) - 2):
            second = first + 1
            third = second + 1
            while second < len(nums) - 1:
                while third < len(nums) and nums[third] < nums[second] + nums[first]:
                    third += 1

                ans += third - second - 1
                second += 1
                third = third if second < third else second + 1
        return ans