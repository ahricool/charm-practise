# 双重循环解法 超时
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                volume = (j - i) * min(height[i], height[j])

                if volume > max_v:
                    max_v = volume
        return max_v


# 2021.12.11
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_volume = 0
        while left < right:
            max_volume = max(min(height[right], height[left]) * (right - left), max_volume)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_volume
