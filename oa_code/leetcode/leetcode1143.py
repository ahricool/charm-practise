

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp=[[0 for _ in range(len(text1))] for _ in range(len(text2))]



