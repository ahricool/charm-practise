class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zero_idx=[]
        left_idx= -1
        max_len=0

        for i in range(len(nums)):
            if nums[i]==0:
                if len(zero_idx)<k:
                    zero_idx.append(i)
                elif k==0:
                    left_idx=i
                else:
                    left_idx=zero_idx.pop(0)
                    zero_idx.append(i)
            max_len=max(max_len,i-left_idx)

        return max_len

            
        