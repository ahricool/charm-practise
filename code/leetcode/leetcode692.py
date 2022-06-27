from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c=Counter(words)
        res=c.most_common(k)
        return res.keys()


