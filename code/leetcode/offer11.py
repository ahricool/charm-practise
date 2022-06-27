import math


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        res=numbers[0]
        while l <= r:
            mid = (l + r) // 2
            res = min(res, numbers[mid])

            # 命中目标 直接返回
            if mid-1>=0 and numbers[mid] < numbers[mid - 1]:
                return numbers[mid]

            if numbers[mid] > numbers[0]:
                l = mid + 1

            elif numbers[mid] < numbers[0]:
                r = mid - 1

            else:
                l = l + 1

        return res



class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]