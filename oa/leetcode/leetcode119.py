class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [0, 1, 0]

        for row in range(1, rowIndex + 1):
            for idx in range(len(ans) - 1):
                ans[idx] = ans[idx] + ans[idx + 1]
            ans.insert(0, 0)
        return ans[1:-1]