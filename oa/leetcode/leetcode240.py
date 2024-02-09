class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx1,idx2=len(matrix)-1,0

        while True:
            if matrix[idx1][idx2]==target:
                return True
            elif matrix[idx1][idx2]<target:
                idx2+=1
            else:
                idx1-=1

            if not ( 0<=idx1<len(matrix) and 0<=idx2<len(matrix[0])):
                return False



