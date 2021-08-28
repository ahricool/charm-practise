# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#
#         nums=sorted(nums)
#
#         for i in range(len(nums)-2):
#



class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        v1 = nums[0]
        v2 = nums[1]
        v3 = nums[2]

        sum = v1 + v2 + v3

        for idx in range(3, len(nums)):

            sub = abs(sum - target)

            sub_1 = abs(sum - v1 + nums[idx] - target)
            sub_2 = abs(sum - v2 + nums[idx] - target)
            sub_3 = abs(sum - v3 + nums[idx] - target)
            min_sub = min(sub_1, sub_2, sub_3)

            if min_sub < sub:
                if sub_1==min_sub:
                    v1=nums[idx]
                elif sub_2==min_sub:
                    v2=nums[idx]
                elif sub_3==min_sub:
                    v3=nums[idx]
            print(v1,v2,v3,v1+v2+v3)
            sum = v1 + v2 + v3
        return sum


print(Solution().threeSumClosest([1,2,4,8,16,32,64,128],88))