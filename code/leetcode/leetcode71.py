class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs=path.split("/")
        ans=[]
        for d in dirs:
            if d=="" or d ==".":
                continue
            elif d=="..":
                if len(ans)>0:
                    ans.pop()
                continue
            else:
                ans.append(d)

        return "/"+"/".join(ans)