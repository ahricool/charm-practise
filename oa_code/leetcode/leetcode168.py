class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber-=1
        ans=[]
        while columnNumber>0:
