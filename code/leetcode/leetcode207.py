class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses={}
        marked=[0 for _ in range(numCourses)]
        self.res=True

        for i in prerequisites:
            courses.setdefault(i[0],[]).append(i[1])


        def mark(k):
            v=courses[k]
            for c in v:
                if marked[c]==1:  ## 已经学完
                    continue

                elif marked[c]==0:  ## 未学
                    marked[c]=2
                    mark(c)
                    marked[c]=1
                    continue
                elif marked[c]==2:  ## 学习中
                    self.res=False
                    continue
        
        for k,v in courses.items():
            if marked[k]==0:
                mark(k)

        return self.res




