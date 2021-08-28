



class Solution:
    sum2 = 0
    def waysToStep(self, n: int) -> int:


        def to_step(n):
            if n>=3:
                to_step(n-3)
            if n>=2:
                to_step(n-2)
            if n>=1:
                to_step(n-1)
            if n==0:
                self.sum2+=1

        to_step(n)

        return self.sum2


# coding=utf-8
import sys

