import functools


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        used = [0 for _ in range(len(wordList))]

        def bfs():
            stack = [(beginWord,1)]
            while stack:
                cur_word,cost=stack.pop(0)
                if cur_word==endWord:
                    return cost
                for idx in range(len(wordList)):
                    if used[idx] == 0 and diff(*sorted([cur_word, wordList[idx]])) == 1:
                        used[idx] = 1
                        stack.append((wordList[idx],cost+1))
            return 0

        # 这个其实是一个 O(n^2)的循环，是非常耗时间的。

        @functools.lru_cache(None)
        def diff(word1, word2):
            count = 0
            for idx in range(min(len(word1), len(word2))):
                if word1[idx] != word2[idx]:
                    count += 1
            return count

        return bfs()

        # 建图的过程是一个需要仔细考虑的过程，如果是用 bitmap 建图，也是需要 O(n^2)的。
        # 如果拆分 str 建图，只需要 O(n)
    