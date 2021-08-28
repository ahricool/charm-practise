class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        tags = [[0 for _ in range(m)] for _ in range(n)]

        x, y = 0, 0
        res = []
        direct = 0
        while True:
            if tags[x][y] == 1:
                break

            tags[x][y] = 1
            res.append(matrix[x][y])

            if direct==0 and  0 <= y <= m - 2 and tags[x][y + 1] == 0:
                direct = 0
                y += 1
                continue
            if direct==1 and 0 <= x <= n - 2 and tags[x + 1][y] == 0:
                direct = 1
                x += 1
                continue
            if direct ==2 and 1 <= y <= m and tags[x][y - 1] == 0:
                direct = 2
                y -= 1
                continue
            if direct==3 and 1 <= x <= n and tags[x - 1][y] == 0:
                direct = 3
                x -= 1
                continue

            if 0 <= y <= m - 2 and tags[x][y + 1] == 0:
                direct = 0
                y += 1
                continue
            if 0 <= x <= n - 2 and tags[x + 1][y] == 0:
                direct = 1
                x += 1
                continue
            if 1 <= y <= m and tags[x][y - 1] == 0:
                direct = 2
                y -= 1
                continue
            if 1 <= x <= n and tags[x - 1][y] == 0:
                direct = 3
                x -= 1
                continue
        return res
