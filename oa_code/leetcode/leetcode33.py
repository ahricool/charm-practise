class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 二分查找的变形，需要考虑的细节很多，如果想清楚写的会很快。
        # 题解有个更清晰的

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                if nums[l] < nums[mid]:  # 左有序
                    l = mid + 1
                    continue
                else:  # 右有序
                    if nums[r] >= target:
                        l = mid + 1
                        continue
                    else:
                        r = mid - 1
                        continue

            if target < nums[mid]:
                if nums[l] <= nums[mid]:  # 左有序
                    if target >= nums[l]:
                        r = mid - 1
                        continue
                    else:
                        l = mid + 1
                        continue
                else:  # 右有序
                    r = mid - 1
                    continue

        return -1
