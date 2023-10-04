class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        len_cur = 0

        def flat():
            if len(cur) == 1:
                res.append(cur[0] + " " * (maxWidth - len(cur[0])))
            else:
                m, n = (maxWidth - len_cur) // (len(cur) - 1), (maxWidth - len_cur) % (len(cur) - 1)

                print(m, n)

                line = ""
                for i in range(len(cur)):
                    line += cur[i]
                    if i < n:
                        line += " " * (m + 1)
                    elif i != len(cur) - 1:
                        line += " " * m

                    print(line)

                res.append(line)

        for index in range(len(words)):
            if len(words[index]) + len_cur + len(cur) > maxWidth:
                flat()
                cur = [words[index]]
                len_cur = len(words[index])
            else:
                cur.append(words[index])
                len_cur += len(words[index])

        if len(cur) != 0:
            line = " ".join(cur)
            res.append(line + " " * (maxWidth - len(line)))

        return res