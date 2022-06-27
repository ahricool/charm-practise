from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(int)

        count=0
        for idx in range(len(time)):
            sec=time[idx]%60
            count+=d[(60-sec)%60]
            d[sec]+=1


        return count