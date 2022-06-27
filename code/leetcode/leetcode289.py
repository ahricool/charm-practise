class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])

        res=[[ 0 for _ in range(m)] for _ in range(n)]

        def getAlive(i,j):
            count=0
            around=[(i-1,j-1),(i-1,j),(i-1,j+1),
                    (i,j-1),(i,j+1),
                    (i+1,j-1),(i+1,j),(i+1,j+1)]
            for current_i,current_j in around:
                if 0<=current_i<=n-1 and 0<=current_j<=m-1:
                    count+=board[current_i][current_j]
            return count

        for i in range(n):
            for j in range(m):
                alive=getAlive(i,j)
                if alive<2 or alive>3:
                    res[i][j]=0
                elif alive==3:
                    res[i][j]=1
                elif alive==2 and board[i][j]==1:
                    res[i][j]=1

        board[:]=res[]


