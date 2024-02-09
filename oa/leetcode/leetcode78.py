# 一个元素要么再集合里面 要么不在  就这两种结果 
# 时间复杂度是 O(2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def next_one(nums,idx,current_set):
            if idx>=len(nums):
                res.append(current_set[:])
                return
            
            current_set.append(nums[idx])
            next_one(nums,idx+1,current_set)
            current_set.pop()
            next_one(nums,idx+1,current_set)
            
            

        next_one(nums,0,[])
        return res