class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix=[[0 for _ in range(n)] for _ in range(n)]
        
        direct=0
        x,y=0,0

        for i in range(1,n*n+1):
            matrix[x][y]=i
            
            if direct==0 
