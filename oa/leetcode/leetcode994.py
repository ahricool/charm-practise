import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 写lfs的题目为什么老想着递归？ 脑子有病
        def lfs(stack):

            max_minutes = 0

            while stack:
                idx1, idx2, minutes = stack.popleft()
                max_minutes = max(max_minutes, minutes)

                neighbors = [(idx1 - 1, idx2), (idx1 + 1, idx2), (idx1, idx2 - 1), (idx1, idx2 + 1)]

                for idx1, idx2 in neighbors:
                    if 0 <= idx1 < len(grid) and 0 <= idx2 < len(grid[0]) and grid[idx1][idx2] == 1:
                        grid[idx1][idx2] = 2
                        stack.append((idx1, idx2, minutes + 1))

            return max_minutes

        stack = collections.deque()
        for idx1 in range(len(grid)):
            for idx2 in range(len(grid[0])):
                if grid[idx1][idx2] == 2:
                    stack.append((idx1, idx2, 0))

        ans = lfs(stack)

        for idx1 in range(len(grid)):
            for idx2 in range(len(grid[0])):
                if grid[idx1][idx2] == 1:
                    return -1

        return ans


