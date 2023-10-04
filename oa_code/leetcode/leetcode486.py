# 使用递归

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        score=self.get(nums,0,len(nums)-1,1)

        return score>=0


    def get(self,nums,l,r,symbol):
        # 只剩下唯一一个数字，必拿
        if l==r:
            return nums[l]*symbol

        # 根据 symbol 判断先后关系
        # 先手 symbol=1 拿到后总分增加，左右中选择总分尽量大的拿
        # 后手 symbol=-1 拿到后总分减少，左右中选择总分尽量小的拿

        get_l=nums[l]*symbol+self.get(nums,l+1,r,-symbol)
        get_r=nums[r]*symbol+self.get(nums,l,r-1,-symbol)

        return max(get_l,get_r) if symbol==1 else min(get_l,get_r)


# 使用动态规划
# 递归中存在大量的重复计算的问题
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        # dp[i][j] 表示 在i->j的数组中开始游戏，当前玩家和另一个玩家分数差的最大值
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # 只剩下一个数字，最大值即为该数字
        for i in range(len(nums)):
            dp[i][i]=nums[i]

        # 转移方程，只依赖左和下两个节点，
        # 所以从下到上，从左到右依次dp
        for j in range(1,len(nums)):
            for i in range(j-1,-1,-1):
                dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])

        return dp[0][-1]>=0


