import math


class Solution:
    def minOperations(self, nums, x: int) -> int:
        self.min_count=math.inf
        def dfs(nums,x,count):
            if x==0:
                self.min_count=min(self.min_count,count)
                return

            if len(nums)==0:
                return


            if nums[-1]<=x:
                value=nums.pop()
                dfs(nums,x-value,count+1)
                nums.append(value)

            if nums[0]<=x:
                value=nums.pop(0)
                dfs(nums, x - value, count + 1)
                nums.insert(0,value)

        dfs(nums,x,0)
        if self.min_count==math.inf:
            return -1
        else:
            return int(self.min_count)


