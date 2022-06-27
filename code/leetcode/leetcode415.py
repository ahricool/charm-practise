# 长短不一的字符串 进行补位操作

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sub_len=len(num1)-len(num2)
        if sub_len>0:
            num2="0"*abs(sub_len)+num2 # 长短不一的字符串 进行补位操作
        else:
            num1="0"*abs(sub_len)+num1

        carry=0
        res=""
        for idx in range(len(num1)-1,-1,-1):
            value=int(num1[idx])+int(num2[idx])+carry
            carry,res=value//10,str(value%10)+res

        if carry:
            res=str(carry)+res
        return res