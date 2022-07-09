import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(start,current):
            for i in range(start,n+1):
                current.append(i)
                if len(current)==k:
                    res.append(copy.copy(current))
                else:
                    dfs(i+1,current)
                current.pop()

        dfs(1,[])
        return res



