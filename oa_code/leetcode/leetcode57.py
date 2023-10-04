

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # def find(l,r, target, idx):
        #     m=(l+r)//2
        #     if intervals[m][idx]>target:
        #

        for i in range(len(intervals)):
            if intervals[i][0]<newInterval[0]<intervals[i][1]:
                return newInterval[0]

            if intervals
