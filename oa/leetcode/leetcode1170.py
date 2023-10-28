import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_count=[]
        for word in words:
            words_count.append(self.countMinLetter(word))
        words_count.sort()
        words_num=len(words)
        ans=[]
        for q in queries:
            q_count=self.countMinLetter(q)
            ans.append(words_num-bisect.bisect_right(words_count,q_count))

            # biset_left returns the largest index to insert the element with respect to <
            # biset_right returns the largest index to insert the element with respect to <=
            
        return ans
            

    def countMinLetter(self,s):
        count=1
        cur=s[0]
        for i in range(1,len(s)):
            if ord(cur)==ord(s[i]):
                count+=1
            elif ord(cur)>ord(s[i]):
                cur=s[i]
                count=1
        return count