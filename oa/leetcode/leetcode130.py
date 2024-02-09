class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        marked=[[0 for _ in range(board[0])] for _ in range(board)]
        def dfs(i,j):
            nonlocal marked
            if board[i][j]=="O":
                marked[i][j]=1



            nxts=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for x,y in nxts:
                dfs(x,y)





        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
