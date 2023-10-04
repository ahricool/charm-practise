from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(list)
        c=0
        for idx in range(len(time)):
            sec=time[idx]%60
            c+=len(d[(60-sec)%60])
            d[sec].append(idx)
        return c
