class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        max_horizontal=max([horizontalCuts[idx]-horizontalCuts[idx-1] for idx in range(1,len(horizontalCuts))])
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        max_vertical=max([verticalCuts[idx]-verticalCuts[idx-1] for idx in range(1,len(verticalCuts))])

        return max_vertical*max_horizontal
