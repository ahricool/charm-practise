class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        row,col=len(matrix)-1,0

        while True:
            if 0<=row<len(matrix) and 0<=col<len(matrix[0]):
                if matrix[row][col]==target:
                    return True
                if matrix[row][0]>target:
                    row-=1
                    continue
                if matrix[row][col]<target:
                    col+=1
                    continue
            else:
                return False