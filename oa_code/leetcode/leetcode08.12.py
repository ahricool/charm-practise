class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen=[]
        count=0
        def put_queen(idx):
            nonlocal count
            if idx==0:
                count+=1

            for i in range(n):
                if i not in queen and is_valid(i):
                    queen.append(i)
                    put_queen(idx-1)
                    queen.pop()

        def is_valid(location):
            for idx in range(len(queen)):
                if abs(queen[idx]-location)==abs(idx-len(queen)):
                    return False
            return True
        put_queen(n)
        return count