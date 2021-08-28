class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1,0,-1):
            large=nums[i]
            for j in range(i-1,-1,-1):
                small=nums[j]
                if large>small:
                    nums[i],nums[j]=small,large
                    return

        nums.reverse()
        return

    