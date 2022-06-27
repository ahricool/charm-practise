from typing import *
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hq = []
        heapq.heapify(hq)
        for cls in classes:
            ratio = (cls[0] + 1) / (cls[1] + 1) - cls[0] / cls[1]
            heapq.heappush(hq, (-ratio, cls[0], cls[1]))

        for _ in range(extraStudents):
            _, cls_pass, cls_total = heapq.heappop(hq)
            cls_pass+=1
            cls_total+=1
            ratio=(cls_pass+1)/(cls_total+1)-cls_pass/cls_total
            heapq.heappush(hq,(-ratio,cls_pass,cls_total))

        return sum(map(lambda cls:cls[1]/cls[2],hq))/len(hq)