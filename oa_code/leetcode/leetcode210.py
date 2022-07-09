import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        edges=collections.defaultdict(list)
        visited=[0]*numCourses
        valid=True
        res=[]

        for l in prerequisites:
            edges[l[1]].append(l[0])

        def dfs(u):
            nonlocal valid
            visited[u]=1

            for v in edges[u]:
                if visited[v]==0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v]==1:
                    valid=False
            visited[u]=2
            res.append(u)


        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        if valid:
            return list(reversed(res))
        else:
            return []
