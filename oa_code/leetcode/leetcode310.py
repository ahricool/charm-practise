class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        height=[0 for _ in range(n)]

        for idx in range(len(edges)):

            
