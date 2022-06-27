# 难点在于如何去重，在结果去重会发现很困难，解决方法时，重新安排搜索顺序，在搜索时进行去重

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def findTarget(start, cur_target, cur_res):
            if cur_target == 0:
                res.append(cur_res[:])
            for index in range(start, len(candidates)):
                if candidates[index] <= cur_target:
                    cur_res.append(candidates[index])
                    findTarget(index, cur_target - candidates[index], cur_res)
                    cur_res.pop()

        findTarget(0, target, [])
        return list(res)
