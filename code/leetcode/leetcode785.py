# 二分图 染色法

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:


        res=True
        marked=[0 for _ in range(len(graph))]
        def dfs(index,mark):
            nonlocal res
            if marked[index]==0:
                marked[index]=mark
                nxt = 2 if mark == 1 else 1
                for i in range(len(graph[index])):
                    dfs(graph[index][i], nxt)
            elif marked[index]==mark:
                return
            else:
                res=False
                return


        for i in range(len(graph)):
            if marked[i]==0:
                dfs(i,1)
        return res






