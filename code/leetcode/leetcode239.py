
# 简单但是会 超时的解法

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_value=max(nums[0:k])
        location=nums.index(max_value)
        slide_max =[max_value,]

        # tips: 首先你要考虑清楚你这个right的定义是什么，是数组的右边界，还是slice的右边界，否则很容易混淆，导致结果很奇怪，这种bug 很难找。
        for right in range(k, len(nums)):
            left=right-k+1
            if nums[right]>=max_value:
                max_value=nums[right]
                location=right
            elif location<left:
                content=nums[left:right+1]
                max_value=max(content)
                location=content.index(max_value)
            slide_max.append(max_value)
        return slide_max


#  优先队列

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
