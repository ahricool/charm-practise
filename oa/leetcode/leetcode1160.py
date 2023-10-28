import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter=collections.Counter(chars)
        
        ans=0
        for w in words:
            w_counter=collections.Counter(w)
            if all(w_counter[c] <= chars_counter[c] for c in w_counter):
                ans+=len(w)

        return ans