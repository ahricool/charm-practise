class Solution:
    def calculate(self, s: str) -> int:
        s=s+"+"

        # 缓存的计算表达式
        stack=[]
        last_symbol="+"
        cur=0
        for i in range(0,len(s)):
            # 是数字
            if s[i].isdigit():
                cur=cur*10+int(s[i])

            # 是符号
            else:
                if last_symbol=="+":
                    stack.append(cur)
                if last_symbol=="-":
                    stack.append(-cur)
                if last_symbol=="//":
                    stack.append(stack.pop(-1)//cur)
                if last_symbol=="*":
                    stack.append(stack.pop(-1)*cur)

                last_symbol=s[i]

        return sum(stack)






