# 写的太乱了。


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_nums= {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        def fill(i,j):
            if board[i][j]==".":
                for num in all_nums-set(board[i]):
                    if check(i,j,num):
                        board[i][j]=num
                        if i==8 and j==8:
                            return board
                        elif i==8:
                            next_i,next_j=0,j+1
                        else:
                            next_i,next_j=i+1,j
                        fill(next_i,next_j)
                return
            else:
                if i == 8 and j == 8:
                    return board
                elif i == 8:
                    next_i, next_j = 0, j + 1
                else:
                    next_i, next_j = i + 1, j
                fill(next_i, next_j)

        def check(i,j,num):
            # check column
            for row in range(9):
                if board[row][j]==num:
                    return False

            # check block
            offset=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
            for n,m in offset:
                row=i//3+n
                col=j//3+m
                if board[row][col]==num:
                    return False

            return True









