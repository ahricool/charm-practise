# dfs算法
# marked 这个矩阵不是必须的，可以优化掉，直接在 grid 这个矩阵上修改

# 也可以用 dfs +栈来做，这样逻辑上更清楚一点

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        marked = [[0 for _ in range(n)] for _ in range(m)]

        max_area = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and marked[i][j] == 0:
                marked[i][j] = 1
                return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1) + 1
            else:
                return 0

        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                max_area = area if area > max_area else max_area # 可以用 max
        return max_area

