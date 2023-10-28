class Solution:
    def countOfAtoms(self, formula: str) -> str:
        s=formula
        stack=[]
        res={}
        for idx in range(len(s)):
            if s[idx].isdigit():
                