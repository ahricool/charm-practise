# 滑动窗口的边界
# slow fast 的含义是什么 必须要考虑的很清楚

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        slow, fast = 0, 0
        max_len = 1
        while fast < len(s):

            if fast + 1 < len(s) and s[fast + 1] in s[slow:fast + 1]:
                while True:
                    slow += 1
                    if s[slow - 1] == s[fast + 1]:
                        break

            fast += 1
            if fast < len(s):
                max_len = max(max_len, fast - slow + 1)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ=set()
        n=len(s)
        slow, fast = 0, 0
        max_len = 0
        for fast in range(n):
            if s[fast] not in occ:
                occ.add(s[fast])
            else:
                while True:
                    slow+=1
                    if s[slow-1]!=s[fast]:
                        occ.remove(s[slow-1])
                    else:
                        break

            max_len = max(max_len, fast - slow + 1)

        return max_len
