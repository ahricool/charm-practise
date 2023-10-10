
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


#  单调栈
#  Python 中真正的链表的实现是 collections.deque()

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s=collections.deque()
        ans=[]
        for idx in range(len(nums)):
            while len(s)!=0 and s[-1]<nums[idx]:
                s.pop()
            s.append(nums[idx])

            if idx>=k-1:
                if idx>=k and nums[idx-k]==s[0]:
                    s.popleft
                ans.append(s[0])  
        return ans

# 这种方法也是正确的，但是在提交的时候回超时，因为Python List 的底层实现是 可变Array
# 在数组长度不断变化的情况在，性能会变得很差。
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s=[]
        ans=[]
        for idx in range(len(nums)):
            while len(s)!=0 and s[-1]<nums[idx]:
                s.pop(-1)
            s.append(nums[idx])

            if idx>=k-1:
                if idx>=k and nums[idx-k]==s[0]:
                    s.pop(0)
                ans.append(s[0])  
        return ans

            

