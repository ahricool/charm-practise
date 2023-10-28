class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = [[] for _ in range(len(mat) + len(mat[0]))]
        for idx1 in range(len(mat)):
            for idx2 in range(len(mat[0])):
                if (idx1 + idx2) % 2 == 1:
                    ans[idx1 + idx2].append(mat[idx1][idx2])
                else:
                    ans[idx1 + idx2].insert(0, mat[idx1][idx2])

        res = []
        for i in ans:
            res += i
        return res




