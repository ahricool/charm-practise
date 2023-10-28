# 典型的回溯算法。

# 参考答案
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)
        # prune
        bc = Counter(board[r][c] for r in range(m) for c in range(n))
        wc = Counter(word)
        for key in wc.keys():
            if wc[key] > bc[key]:
                return False

        visited = [[False for _ in range(n)] for _ in range(m)]

        # curr at (row, col), need to fill idx
        def backtrack(row, col, idx):
            if idx == w:
                return True
            visited[row][col] = True
            for r, c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if m > r >= 0 and n > c >= 0 and not visited[r][c] and board[r][c] == word[idx]:
                    if backtrack(r, c, idx + 1): return True
            visited[row][col] = False

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1):
                    return True
        return False


# 自己写的
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        visited=[[False for _ in range(m)] for _ in range(n)]

        def dfs(x,y,idx):
            if idx>=len(word):
                return True
            if n>x>=0 and m>y>=0 and visited[x][y]==False:
                if board[x][y]==word[idx]:
                    visited[x][y]=True
                    for x_next,y_next in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                        if dfs(x_next,y_next,idx+1):
                            return True
                    visited[x][y]=False
                    return False
        for x in range(n):
            for y in range(m):
                if dfs(x,y,0):
                    return True
        return False
























