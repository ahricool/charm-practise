class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def nextSet(nums,start,current_set):
            res.append(current_set[:])
            for index in range(start,len(nums)):
                current_set.append(nums[index])
                nextSet(nums,index,current_set)
                current_set.pop()

        nextSet(nums,0,[])
        return res