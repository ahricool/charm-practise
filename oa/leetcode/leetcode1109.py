
# 简单直白的做法，但是这种会超时
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0 for _ in range(n)]
        for booking in bookings:
            for air in range(booking[0],booking[1]+1):
                ans[air]+=booking[2]
        return ans

# 差分数组

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]
        for b in bookings:
            ans[b[0] - 1] += b[2]
            ans[b[1]] -= b[2]
        s = 0
        for idx in range(len(ans)):
            ans[idx] = s = s + ans[idx]
        return ans[:-1]
