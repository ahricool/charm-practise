class Solution:
    def romanToInt(self, s: str) -> int:

        map={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=0
        for index in range(len(s)):
            if index+1<len(s) and map[s[index]]<map[s[index+1]]:
                res-=map[s[index]]
            else:
                res+=map[s[index]]
        return res


