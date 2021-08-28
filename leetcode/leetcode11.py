class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                volume = (j - i) * min(height[i], height[j])

                if volume > max_v:
                    max_v = volume
        return max_v
