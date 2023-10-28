class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals=sorted(intervals,key=lambda x:x[0])
        res=[]
        pre=intervals[0]
        for idx in range(1,len(intervals)):
            cur=intervals[idx]
            if cur[0]>pre[1]: # can't merge
                res.append(pre)
                pre=cur
                continue
            elif cur[1]<=pre[1]:
                continue
            elif cur[1]>pre[1]:
                pre[1]=cur[1]
                continue

        res.append(pre)
        return res
