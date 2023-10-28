
# diff 类似差分数组

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        diff = [0 for _ in range(26)]
        ans = []
        for i in p:
            diff[ord(i) - ord("a")] -= 1

        for idx in range(len(s)):
            diff[ord(s[idx]) - ord("a")] += 1

            if idx - n >= 0:
                diff[ord(s[idx-n]) - ord("a")] -= 1

            if not any(diff):
                ans.append(idx-n+1)

        return ans
