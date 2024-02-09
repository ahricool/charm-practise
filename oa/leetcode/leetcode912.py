import random



# 快速排序

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l >= r:
            return

        pivot_idx = random.randint(l, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

        pivot = nums[r]  # 选最后一个做pivot
        idx = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[r] = nums[r], nums[idx]

        self.quickSort(nums, l, idx - 1)
        self.quickSort(nums, idx + 1, r)



# 冒泡排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
