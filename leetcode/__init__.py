# 01.01

class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) > 24:
            return False
        for index1, c in enumerate(astr):
            for index2 in range(index1 + 1, len(astr)):
                if astr[index1] == astr[index2]:
                    return False

        return True

# 执行用时：40 ms, 在所有 Python3 提交中击败了61.75% 的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.94%

# Option2

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        a=[0]*26
        for i in s1:
            a[ord(i)-ord("a")]+=1
        for i in s2:
            a[ord(i)-ord("a")]-=1
        return a==[0]*26

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S.strip(" ")
        return S.replace(" ","%20")

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        a=len(first)
        b=len(second)
        if not -1<=a-b<=1:
            return False

        index1,index2=0,0
        count=0
        while(index1<a and index2<b):
            if(first[index1]==second[index2]):
                index1+=1
                index2+=1
            elif(first[index1+1]==second[index2]):
                index1+=2
                index2+=1
                count+=1
            elif(first[index1]==second[index2+1]):
                index1+=1
                index2+=2
                count+=1

            if count==2:
                return False


class Solution:
    def compressString(self, S: str) -> str:
        pass


class Solution:
    def missingTwo(self, nums: list[int]) -> list[int]:
        nums.insert(0, 0)
        nums.extend([-1, -1])
        index = 0
        while (index < len(nums)):
            if index == nums[index] or nums[index]==-1:
                index += 1
            else:
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
        loss=[]
        for index in range(len(nums)):
            if nums[index]==-1:
                loss.append(index)
        return loss

a=[1,2,3,4,7,8,1,1]
for n in a:
    a[3]+=1
    print(n)

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes=boxes.sort(reverse=True)
        count=0
        index1,index2=0,0
        while(index1<len(boxes) and index2<len(warehouse)):
            if boxes[index1]<=warehouse[index2]:
                count+=1
                index1+=1
                index2+=1
            else:
                index1+=1

        return count

