class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[ 0 for _ in range(num_people)]
        cur=1
        while True:
            idx=(cur-1)%num_people
            if candies>=cur:
                res[idx]+=cur
                candies-=cur
            else:
                res[idx]+=candies
                return res



