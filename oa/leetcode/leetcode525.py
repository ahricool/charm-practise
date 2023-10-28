class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和+哈希表 前缀和容易想到
        # 在数组中找某两个相互关联的值  一定要想到 哈希表

        # prefix_sum 和循环都可以优化掉

        prefix_sum = []
        sum_value = 0
        for i in nums:
            sum_value += 1 if i == 1 else -1
            prefix_sum.append(sum_value)
        print(prefix_sum)
        prefix_sum.insert(0, 0)  # 边界条件之一
        max_len = 0
        d = {}
        for idx in range(len(prefix_sum)):
            if prefix_sum[idx] in d.keys():
                max_len = max(idx - d[prefix_sum[idx]], max_len)
            else:
                d[prefix_sum[idx]] = idx

        return max_len


