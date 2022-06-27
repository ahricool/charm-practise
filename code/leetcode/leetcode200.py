# dfs 可以秒杀

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        tags=[[0 for _ in range(m)] for _ in range(n)]
        count=0

        def mark(i,j):
            if tags[i][j]==1:
                return
            tags[i][j]=1
            if grid[i][j]=="1":
                if i>0:
                    mark(i-1,j)
                if i<n-1:
                    mark(i+1,j)
                if j<m-1:
                    mark(i,j+1)
                if j>0:
                    mark(i,j-1)


        for i in range(n):
            for j in range(m):
                if tags[i][j]==0 and grid[i][j]=="1":
                    count+=1
                    mark(i,j)


        return count