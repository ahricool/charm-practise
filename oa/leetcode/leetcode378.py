
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r=matrix[0][0],matrix[-1][-1]
        while l<=r:
            mid=(l+r)//2
            if self.smallerX(matrix,mid)>=k:
                r=mid-1
            else:
                l=mid+1
        return (l+r)//2

    def smallerX(self,matrix,X):
        count=0
        col=0
        for row in range(len(matrix)-1,-1,-1):
            if 0<=col<len(matrix[0]) and matrix[row][col]<=X:
                col+=1
            count+=col
        return count




