import math
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for idx in range(len(timePoints)):
            t=timePoints[idx].split(":")
            timePoints[idx]=int(t[0])*60+int(t[1])

        timePoints.sort()
        
        min_time=math.inf
        for idx in range(len(timePoints)-1):
            min_time=min(min_time,timePoints[idx+1]-timePoints[idx])
            
        min_time=min(min_time,24*60+timePoints[0]-timePoints[-1])

        return min_time
            