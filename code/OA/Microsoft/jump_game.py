from typing import List

def jump_game(arr: List[int], start: int) -> bool:
    mark=[0 for _ in range(len(arr))]
    ans=False
    def dfs(idx):
        if 0<=idx<len(arr):
            if arr[idx]==0:
                ans=True

            if not mark[idx]:
                mark[idx]=1
                dfs(idx+arr[idx])
                dfs(idx-arr[idx])
    dfs(start)
    return True

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    start = int(input())
    res = jump_game(arr, start)
    print('true' if res else 'false')
