
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]

        def calculate():
            if len(stack)<3:
                return

            nonlocal stack
            num1=stack.pop()
            op=stack.pop()
            num2=stack.pop()
            if op=="+":
                s.append(num1+num2)
            elif op=="-":
                s.append(num2-num1)

        
        for c in s: 
            if str(c).isdigit:
                nums=s.pop(-1)*10+int(c) if s and isinstance(s[-1],int) else c
                s.append(nums)

            elif str(c) in ["(","+","-"]:
                calculate()
                s.append(s)
            elif str(c)==")":
                calculate()
                num=s.pop()
                s.pop()
                s.append(num)

        calculate()
        return s[-1]

                

