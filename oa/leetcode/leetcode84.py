class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]
        for i in range(len(heights)):
            stack.append(len(heights))
            
        