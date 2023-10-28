class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        idx = 0

        while idx < len(asteroids):
            i = asteroids[idx]
            # 会相撞
            if ans and ans[-1] > 0 > i:
                if abs(ans[-1]) > abs(i):
                    idx+=1
                elif abs(ans[-1]) < abs(i):
                    ans.pop()
                else:
                    ans.pop()
                    idx+=1
            # 不会相撞
            else:
                ans.append(i)
                idx+=1

        return ans
