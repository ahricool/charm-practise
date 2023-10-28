class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def swap(idx):

            if nums[idx] != idx + 1 and 0 < nums[idx] <= len(nums):
                if nums[nums[idx] - 1] != nums[idx]:
                    idx2 = nums[idx] - 1
                    nums[idx], nums[idx2] = nums[idx2], nums[idx]

                    swap(idx)

        for i in range(len(nums)):
            swap(i)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return nums[-1] + 1
