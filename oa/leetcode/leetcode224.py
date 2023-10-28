
class Solution:
    def calculate(self, s: str) -> int:


        stack=[]

        def calculate():
            nonlocal stack
            if len(stack)>=3: 
                if stack[-2] in ["+","-"] and isinstance(stack[-1],int) and isinstance(stack[-3],int):
                    num1=stack.pop()
                    op=stack.pop()
                    num2=stack.pop()
                    if op=="+":
                        stack.append(num1+num2)
                    elif op=="-":
                        stack.append(num2-num1)
                
            

        for c in s:

            # Process numbers
            if str(c).isdigit():
                print(stack)
                nums=int(c)
                if stack and isinstance(stack[-1],int):
                    nums=stack.pop(-1)*10+nums
                stack.append(nums)

            # Process operator
            elif str(c) in ["(","+","-"]:
                print(stack)
                calculate()
                stack.append(c)

            elif str(c)==")":
                print(stack)
                calculate()
                num=stack.pop()

                stack.pop() # 弹出左括号
                stack.append(num)

        calculate()
        return stack[-1]






# 先把字符串转为逆波兰表达式，再根据逆波兰表达式求解运算。

class Solution:
    def calculate(self, s: str) -> int:
        
        reverse_polish_expression=[]

        for idx in range(len(s)):
            if s[idx].isdigit():
                
