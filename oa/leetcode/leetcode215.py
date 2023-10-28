import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=[]
        heapq.heapify(a)
        for i in nums:
            heapq.heappush(a,i)
            if len(a)>k:
                heapq.heappop(a)

        return heapq.heappop(a)

