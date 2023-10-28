# 两种思路 1 第一遍遍历 先吧 2 弄到尾部  第二遍遍历，再把1 弄到头部

# 弄两个指针 分别指向 ptr1 和 ptr2



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ptr1=-1
        ptr2=-1

        for i in range(len(nums)):
            if nums[i]==1:
                if i-1>=0:
                    nums[i]=nums[i-1]
                ptr2+=1
                nums[ptr2]=1
                continue

            if nums[i]==0:

                if i-1>=0:
                    nums[i]=nums[i-1]

                ptr2+=1
                nums[ptr2]=1
                ptr1+=1
                nums[ptr1]=0

        return nums