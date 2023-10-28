import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(list)
        s = 0
        ans = 0

        # 倒排 前缀和哈希表
        for index in range(len(nums)):
            s += nums[index]
            d[s].append(index)

        d[0].append(-1)

        # 分情况讨论，有几种比较复杂
        # 复杂度提升的原因是因为需要看idx的先后顺序。实际上在前缀和构建的过程中就可以算出所有的顺序。
        for key in d.keys():
            if k == 0:
                l = len(d[key])
                ans += l * (l - 1) // 2
            if k != 0 and key - k in d:
                for idx1 in d[key]:
                    for idx2 in d[key - k]:
                        if idx1 > idx2:
                            ans += 1

        return ans


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(list)
        s = 0
        ans = 0

        d[0].append(-1)

        # 倒排 前缀和哈希表
        for index in range(len(nums)):
            s += nums[index]

            if s-k in d.keys():
                ans+=len(d[s-k])

            d[s].append(index)



        return ans