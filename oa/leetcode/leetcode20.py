class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sign = {"(": ")",
                "{": "}",
                "[": "]"}

        for i in s:
            if i in sign.keys():
                if len(stack) > 0 and stack[-1] == sign.get(i):
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)

        return len(stack)==0
