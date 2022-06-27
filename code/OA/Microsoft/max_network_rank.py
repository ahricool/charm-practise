from typing import List

from collections import defaultdict

def max_network_rank(starts: List[int], ends: List[int], n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    d=defaultdict(int)
    for i in starts+ends:
        d[i]+=1

    rank=0
    for idx in range(len(starts)):
        road_nums=d[starts[idx]]+d[ends[idx]]
        rank=max(rank,road_nums-1)

    return rank




if __name__ == '__main__':
    starts = [int(x) for x in input().split()]
    ends = [int(x) for x in input().split()]
    n = int(input())
    res = max_network_rank(starts, ends, n)
    print(res)