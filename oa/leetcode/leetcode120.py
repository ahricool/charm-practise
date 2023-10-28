class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for row in range(1,len(triangle)):
            for idx in range(len(triangle[row])):
                if idx==0:
                    triangle[row][idx]+=triangle[row-1][idx]
                elif idx==len(triangle[row])-1:
                    triangle[row][idx]+=triangle[row-1][-1]
                else:
                    triangle[row][idx]+=min(triangle[row-1][idx],triangle[row-1][idx-1])

        return min(triangle[-1])
