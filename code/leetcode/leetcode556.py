import math


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 下一个排列怎么生成  想清楚

        # 不要想当然  然后不断的犯错
        s=list(str(n))
        cur=len(s)-1
        for idx in range(len(s) - 2, -1, -1):
            if int(s[idx]) < int(s[cur]):
                swap_idx=cur
                for i in range(idx+1,len(s)):
                    if int(s[idx])<int(s[i])<int(s[swap_idx]):
                        swap_idx=i
                s[idx], s[swap_idx] = s[swap_idx], s[idx]
                ret=int("".join(s[0:idx+1]+sorted(s[idx+1:])))
                print(ret)
                return ret if ret<2**31 else -1
            else:
                cur=idx

        return -1