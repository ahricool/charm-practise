class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        alpha_count = {}
        stack = []
        for index in range(len(s)):
            alpha_count[s[index]] = alpha_count.get(s[index], 0) + 1

        for i in s:
            alpha_count[i] -= 1

            # 栈为空
            if i not in stack:

                while stack and ord(i) < ord(stack[-1]) and alpha_count[stack[-1]] != 0:
                    stack.pop()
                stack.append(i)

        return "".join(stack)