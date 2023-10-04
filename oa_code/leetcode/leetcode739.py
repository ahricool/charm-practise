class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递减栈
        s=[(temperatures[0],0)]
        ans=[0 for _ in range(len(temperatures))]
        for idx in range(1,len(temperatures)):

            if len(s)>0 and temperatures[idx]>s[-1][0]: # 温度升高

                while len(s)>0 and temperatures[idx]>s[-1][0]:
                    ans[s[-1][1]]=idx-s[-1][1]
                    s.pop(-1)

            s.append((temperatures[idx],idx))
        
        return ans
    

# 这里如果s栈内存储的索引会进一步减少空间，
# 单调栈并不一定栈内的数据是单调的，栈内的数据可能是索引


                

        