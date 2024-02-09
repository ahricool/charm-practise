#  需要额外空间

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy
        d=numpy.array(matrix)
        d=numpy.rot90(d,k=-1).tolist() 
        for i in range(len(d)):
            for j in range(len(d[0])):
                matrix[i][j]=d[i][j]


#   不需要额外空间

# 先上下翻转  然后再对角翻转
                        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        

        