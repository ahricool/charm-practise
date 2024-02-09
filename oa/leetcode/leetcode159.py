import heapq


# 堆的用法
# heapq.heapify(x) 将x变成堆，x对象是啥结果还是啥，就是对其中的元素进行了一次堆排序
# heapq.heappush(x,i)  将i放入堆中
# heapq.heappop(x) 将堆顶元素弹出  和一般的排序算法一样  heapq 也是从小到大进行排序的  堆顶是最小的元素
# heapq.heapreplace(x,i) 将x中最小元素弹出，并且将i 放入

class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        ans=[-i for i in stock[0:cnt]]
        heapq.heapify(ans)  # 变成一个堆
        for i in stock[cnt:]:
            heapq.heappush(ans,-i)  # 因为我们要找 stock 中最小几个值，在这个过程中弹出大的值，所以应该存入负数
            heapq.heappop(ans)  # 弹出最小的元素
        return [ -i for i in ans]
