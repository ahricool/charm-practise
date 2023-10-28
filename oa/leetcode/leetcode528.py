class Solution:

    def __init__(self, w: List[int]):
        self.total=0
        self.prefix_sum=[]
        for weight in w:
            self.prefix_sum.append(self.total)
            self.total+=weight
        self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        import random
        r=random.randint(1,self.total)
        for idx in range(len(self.prefix_sum)):
            if self.prefix_sum[idx]<r<=self.prefix_sum[idx+1]:
                return idx



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()