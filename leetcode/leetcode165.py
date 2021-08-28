class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        lens=max(len(v1),len(v2))
        for i in range(lens):
            n1,n2=int(v1[i]) if i<len(v1) else 0 ,int(v2[i]) if i<len(v2) else 0
            if n1>n2:
                return 1
            if n1<n2:
                return -1

        return 0