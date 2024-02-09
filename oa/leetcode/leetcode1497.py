class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        nums=[]
        zero_counter=0
        for i in range(len(arr)):
            n=arr[i]%k
            if n==0:
                zero_counter+=1
            else:
                nums.append(n)
        if zero_counter%2==1:
            return False
        arr=nums
        arr.sort()
        for i in range(len(arr)//2):
            if (arr[i]+arr[len(arr)-1-i])%k!=0:
                return False

        if len(arr)%2==1 and arr[len(arr)//2+1]%k!=0:
            return False

        return True

