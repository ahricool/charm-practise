class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_index={}
        stack=[]
        for index in range(len(s)):
            last_index[s[index]]=index
        
        for index in range(len(s)):
            if len(stack)==0 or ord(s[index]) < 

        return