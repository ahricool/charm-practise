
class Solution:
    def decodeString(self, s: str) -> str:

        """
        输入：s = "3[a2[c]]"
        输出："accaccacc"
        """
        stack = []
        digit = ""
        for idx in range(len(s)):
            if s[idx] == "]":
                decoded = ""
                while len(stack) > 0:
                    decoded = stack.pop() + decoded
                    if decoded[0]=="[":
                        decoded = decoded[1:] * int(stack.pop())
                        break
                stack.extend(list(decoded))
            elif s[idx].isdigit():
                digit = digit + s[idx]
            elif s[idx]=="[":
                stack.append(digit)
                digit=""
                stack.append("[")
            else:
                stack.append(s[idx])
        return "".join(stack)
