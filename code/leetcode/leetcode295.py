import sortedcontainers

class MedianFinder:

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