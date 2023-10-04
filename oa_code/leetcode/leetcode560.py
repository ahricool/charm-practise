import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(list)
        s = 0
        ans = 0
        # 构造前缀和   哈希表
        for index in range(len(nums)):
            s += nums[index]
            d[s].append(index)

        # 分情况讨论，有几种比较复杂
        for key in d.keys():
            if k==0 and key==0:
                ans+=len(d[key])
            if k==0 and key!=0:
                l=len(d[key])
                ans+=l*(l-1)//2
            if k!=0 and key-k in d:
                ans+=len(d[key])*len(d[key-k])

        return ans
