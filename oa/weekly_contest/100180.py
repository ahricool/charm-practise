class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        max_values=[]
        edge=[]
        mvalue=0
        for num in nums:
            edge.append(num)
            