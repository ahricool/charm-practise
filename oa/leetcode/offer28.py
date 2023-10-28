

class Solution:
    def permutation(self, s: str) -> List[str]:
        ans=set()
        chars=list(s)

        def nxt(chars,cur):
            if len(chars)==0:
                ans.add("".join(cur))
            for idx in range(len(chars)):
                value=chars.pop(idx)
                cur.append(value)
                nxt(chars,cur)
                cur.pop()
                chars.insert(idx,value)

        nxt(chars,[])
        return list(ans)
