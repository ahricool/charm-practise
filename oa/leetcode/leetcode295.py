import sortedcontainers

class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=sortedcontainers.SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        idx,mod=len(self.data)//2,len(self.data)%2
        if mod==1:
            return self.data[idx]
        else:
            return (self.data[idx-1]+self.data[idx])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]


    def addNum(self, num: int) -> None:
        # 比小根堆最小的值要大
        if self.min_heap[0]<=num:
            heapq.heappush(self.min_heap,num)
            if len(self.min_heap)-len(self.max_heap)>1:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        # 比大根堆最大值的值要小
        else:
            heapq.heappush(self.max_heap, -num)
            if len(self.min_heap) - len(self.max_heap) <0:
                heapq.heappush(self.min_heap, -heapq.heappop(self. max_heap))



    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0])/2
        return self.min_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()