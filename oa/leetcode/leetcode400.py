class Solution:
    def findNthDigit(self, n: int) -> int:


    def getRank(n):
        s=str(n)
        count=0
        cur=9
        while cur<=n:
            count+=len(str(cur))*9*(10**(len(str(cur))))
            cur=cur*10+9

        return count