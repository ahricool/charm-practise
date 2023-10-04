class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negative = False if s[0].isdigit() or s[0]=="+" else False
        value = 0
        for c in s:
            if c =="+" or c=="-":
                negative = True
            elif c == "+":
                pass
            else:
                try:
                    num = int(c)
                except:
                    break
                value = value * 10 + num
        if negative:
            value = -value

        if value < -2 ** 31:
            value = -2 ** 31
        if value > 2 ** 31 - 1:
            value = 2 ** 31 - 1
        return value
