
import collections


class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        d=collections.defaultdict(int)
        for i in range(len(answers)):
            d[answers[i]]+=1

        all_count=0
        for key,value in d.items():
            count=key+1
            all_count=count*(value//count+1)

        return all_count

