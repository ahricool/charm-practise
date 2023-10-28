class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:

        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dp[0][0]=matrix[0][0]

