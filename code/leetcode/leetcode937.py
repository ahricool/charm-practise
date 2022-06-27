from typing import List

class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)




class Solution(object):
    def reorderLogFiles(self, logs):
        alphabet=[]
        nums=[]
        for log in logs:
            id_,content=log.split(" ",1)
            if str(content[0]).isalpha():
                alphabet.append((id_,content))
            else:
                nums.append((id_,content))
        alphabet.sort(key=lambda x:x[1])
        return ["{} {}".format(i[0],i[1]) for i in alphabet+nums]
