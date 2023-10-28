class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = []
        for i in num:
            while k > 0 and nums and int(nums[-1]) > int(i):
                nums.pop()
                k -= 1
            nums.append(i)

        while k > 0:
            nums.pop()
            k -= 1

        while nums and nums[0] == "0":
            nums.pop(0)
        if not nums:
            return "0"

        return "".join(nums)


