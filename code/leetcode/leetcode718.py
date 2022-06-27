class Solution:

    # 滑动窗口 和 dp 都可以做
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1,len2=len(nums1),len(nums2)
        dp=[[0 for _ in range(len1)] for _ in range(len2)]

        for i in range(len1):
            if nums2[0]==nums1[i]:
                dp[0][i]=1
        for j in range(len2):
            if nums1[0]==nums2[j]:
                dp[j][0]=1

        for i in range(1,len1):
            for j in range(1,len2):
                if nums2[j]==nums1[i]:
                    dp[j][i]=dp[j-1][i-1]+1

        return max([max(row) for row in dp])
