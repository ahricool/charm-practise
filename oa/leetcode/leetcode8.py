class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negative = False
        if not s[0].isdigit:
            if s[0] in ["+","-"]:
                if s[0]=="-":
                    negative=True 
                s=s[1:]
            else:
                return 0
            
        value = 0
        for c in s:
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
