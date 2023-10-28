
# 回溯 会超时

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:



        def locate(s,wordDict,index):
            if index>=len(s):
                return True
            for i in range(index,len(s)):
                current_str=s[index:i+1]
                if current_str in wordDict:
                    if locate(s,wordDict,i+1):
                        return True
            return False

        return locate(s,wordDict,0)



# DP
# 对于边界条件比较复杂，可以设置dummy 的边界

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp=[0 for _ in range(len(s)+1)]
        dp[0]=1 # dummy 边界
        for idx in range(1,len(dp)):
            for i in range(idx):
                if dp[i]==1 and dp[idx]==0 and s[i:idx] in wordDict:
                    dp[idx]=1

        return bool(dp[-1])




