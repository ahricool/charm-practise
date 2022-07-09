class Solution:
    def longestPalindrome(self, s: str) -> str:

        res=[]

        def check(i, j, current):
            if i<0 or j >=len(s):
                return

            if s[i] == s[j]:
                current.append(s[j])
                current.insert(0, s[i])
                check(i - 1, j + 1, current)

        for i in range(len(s)):
            cur1 = [s[i], ]
            check(i - 1, i + 1, cur1)
            cur2 = []
            check(i, i + 1, cur2)

            len1,len2=len(cur1),len(cur2)
            if len(res)<max(len1,len2):
                if len1>len2:
                    res=cur1
                else:
                    res=cur2
        return "".join(res)
