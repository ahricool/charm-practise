class Solution:
    def maximumSwap(self, num: int) -> int:
        max_value=num
        s=str(num) # 将数字转换为 list 比 str更容易处理  因为 Str是不可变对象
        for i in range(len(s)-1,0,-1):
            for j in range(i):
                swapped=s[0:j]+s[i]+s[j+1:i]+s[j]+s[i+1:]
                max_value=int(swapped) if int(swapped)>max_value else max_value

        return max_value

