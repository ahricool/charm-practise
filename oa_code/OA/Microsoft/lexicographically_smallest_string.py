def smallest_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    for idx in range(len(s)-1):
        if ord(s[idx])>ord(s[idx+1]):
            return s[0:idx]+s[idx+1:]


    return s[0:-1]

if __name__ == '__main__':
    s = input()
    res = smallest_string(s)
    print(res)