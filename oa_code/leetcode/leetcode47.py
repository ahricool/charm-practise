class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        ans = []

        self.dfs(nums,[],ans)
        return ans

    def dfs(self, nums, cur, res):
        # 递归出口 添加最后结果
        if len(nums) == 0:
            res.append(cur[:])

        # 处理当前元素
        pre = None
        for index in range(len(nums)):
            number = nums[index]

            if number == pre:
                continue

            cur.append(number)
            pre = number
            nums.pop(index)
            self.dfs(nums, cur, res)
            nums.insert(index, number)
            cur.pop(-1)
