# 这道题编码不难，难的是把事实想通，知道 下一个排列 究竟是什么玩意。

# 文字很难描述清楚，需要多写几个 下一个排列 来发现规律
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1, 0, -1):  # 注意第二个参数，如果你想循环到0的话，要填-1,这里会循环到1
            if nums[i] > nums[i - 1]:  # 找到第一个顺序对
                for idx in range(len(nums)-1,i-1,-1):
                    if nums[idx]>nums[i-1]:    # 找到能替换顺序对的最小的元素
                        nums[i - 1], nums[idx] = nums[idx], nums[i - 1]  # 交换元素
                        nums[i:] = sorted(nums[i:])   # 对之后的元素排序
                        return

        nums.reverse()
        return
