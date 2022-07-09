class Solution:
    def hammingWeight(self, n: int) -> int:

        bin_n=bin(n)
        s=str(bin_n)

        return len(s.split("1"))-1
