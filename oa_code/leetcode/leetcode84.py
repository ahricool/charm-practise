class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        dp=[[0,0] for _ in range(len(heights))]
        