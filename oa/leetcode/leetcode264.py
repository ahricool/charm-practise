import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[]
        heapq.heappush(heap,1)
        for i in range(n):
            ugly=heapq.heappop(heap)
        