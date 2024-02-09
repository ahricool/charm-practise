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


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # 建立堆排序，默认的是小根堆，即堆顶为最小元素
        ans = nums[0:k]
        heapq.heapify(ans)
        for i in range(k, len(nums)):
            # 将元素放入小根堆，并将小根堆中最小的元素弹出，这样堆中保留的总是前k个最大值
            heapq.heappush(ans, nums[i])
            heapq.heappop(ans)
        # 将堆中最小元素弹出，即第k个最大值
        return heapq.heappop(ans)


