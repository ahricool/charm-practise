class Solution:
    def trap(self, height: List[int]) -> int:
        max_val=max(height)
        max_idx=height.index(max_val)

        total_val=0
        ptr1=0
        for i in range(max_idx):
            if ptr1<height[i]:
                ptr1=height[i]
                continue
            else:
                total_val+=ptr1-height[i]

        ptr2=0
        for i in range(len(height)-1,max_idx,-1):
            if ptr2<height[i]:
                ptr2=height[i]
                continue
            else:
                total_val+=ptr2-height[i]

        return total_val


