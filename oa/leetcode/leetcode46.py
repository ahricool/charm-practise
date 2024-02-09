class Solution:
    def permute(self, nums) :
        l = len(nums)
        res=[]
        import copy

        def find_other(row):

            if len(row)==l:
                res.append(row)
                print(row)
                return
            for k in range(l):
                if nums[k] not in row:
                    apd_row = copy.copy(row)
                    apd_row.append(nums[k])
                    find_other(apd_row)
                else:
                    continue

        for i in range(l):
            row=[nums[i],]
            find_other(row)
        return res







