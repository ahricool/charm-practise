
# 根据讨论的结果，只需要找出最大三个数和最小两个数即可。
# 可以排序找，时间复杂度会略高
# 最佳方式是线性扫描

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        
        nums=sorted(nums)
        n=len(nums)

        # 全为负
        if nums[-1]<0:
            return nums[-1]*nums[-2]*nums[-3]
        # 全为正
        if nums[0]>=0:
            return nums[-1]*nums[-2]*nums[-3]
        
        # 至少有两个负数:
        if nums[-1]>=0 and nums[1]<0:
            return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
        
        # 只有一个负数：
        if nums[1]>=0 and nums[0]<0:
            return nums[-1]*nums[-2]*nums[-3]
        


