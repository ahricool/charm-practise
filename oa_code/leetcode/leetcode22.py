class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def generate(lc,rc,s):
            if lc==0 and rc==0:
                ans.append(s)
                return
            if lc>0:
                generate(lc-1,rc,s+"(")

            if rc>0 and lc<rc:
                generate(lc,rc-1,s+")")

        generate(n,n,"")
        return ans

            

