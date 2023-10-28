

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for i in t:
            target[i] = target.setdefault(i, 0) + 1

        slow, fast = 0, 0
        res = s + "0"

        if s[0] in target:
            target[s[0]]-=1

        while fast < len(s):
            if all(map(lambda x: x <= 0, target.values())):
                while slow<=fast:
                    if len(res) > fast - slow + 1:
                        res = s[slow:fast + 1]
                    if s[slow] in target:
                        target[s[slow]]+=1
                        slow += 1
                        break
                    slow += 1
            else:
                fast+=1
                if fast<len(s) and s[fast] in target:
                    target[s[fast]]-=1
                    # print(target)


        #
        # while fast<len(s):
        #     if all(map(lambda x:x<=0,target.values())):
        #         if len(res)>fast-slow+1:
        #             res=s[slow:fast+1]
        #         if s[slow] in target:
        #             target[s[slow]]+=1
        #         slow+=1
        #     else:
        #         fast += 1
        #         if fast<len(s) and s[fast] in target:
        #             target[s[fast]]-=1
        #

        return "" if len(res)>len(s) else res

