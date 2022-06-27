def split_primes(input_str: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    primes=set()
    for i in range(2,1001):
        if all([ i%p for p in primes]):
            primes.add(i)

    dp=[0]*len(input_str)
    for i in range(len(dp)):
        count=0
        for j in range(-1,i):
            if input_str[j+1]==0:
                continue
            num=int(input_str[j+1:i+1])
            if 2<=num<=1000 and num in primes:
                count+=dp[j] if j!=-1 else 1
        dp[i]=count



    return dp[-1]

if __name__ == '__main__':
    input_str = input()
    res = split_primes(input_str)
    print(res)
