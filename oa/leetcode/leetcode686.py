class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_count=0
        cur_count=1
        for index in range(1,len(s))








class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=0
        for index in range(len(s)-1):
            if s[index]!=s[index+1]:
                first=index
                second=index+1
                while first>=0:
                    if first>=0 and second<len(s) and s[first]==s[index] and s[first]!=s[second]:
                        count+=1
                        first-=1
                        second+=1
                    else:
                        break
        return count
