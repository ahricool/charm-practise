m = {
    "1": "Yi",
    "2": "Er",
    "3": "San",
    "4": "Si",
    "5": "Wu",
    "6": "Liu",
    "7": "Qi",
    "8": "Ba",
    "9": "Jiu",
    "0": "Ling",
}

m = {
    "1": "Yi",
    "2": "Er",
    "3": "San",
    "4": "Si",
    "5": "Wu",
    "6": "Liu",
    "7": "Qi",
    "8": "Ba",
    "9": "Jiu",
    "0": "Ling",
}


def toPinyin(num):
    ans = ""
    s = str(num)
    unit = ["Yi", "Wan", ""]
    while p:=s[-4:len(s)]:
        if int(p) == 0:
            ans = "Ling" + ans
            continue
        p = "0" * (4 - len(p)) + p
        tmp = toRead(p)
        ans = tmp + unit.pop() + ans
        s=s[0:-4]

    if ans.startswith("Ling"):
        ans=ans[4:]
    if ans.endswith("Ling"):
        ans=ans[0:-4]
    return ans


def toRead(num):
    # len(num)==4
    # 4003
    s = ""
    unit = ["Qian", "Bai", "Shi", ""]
    for idx in range(len(num)):
        if num[idx] == "0" and s[-4:len(s)]== "Ling":
            continue
        if num[idx] == "0":
            s += "Ling"
        else:
            s += m[num[idx]] + unit[idx]

    p = s[-4:len(s)]
    # 10000000
    if p == "Ling":
        return s[0:-4]
    else:
        return s


print(toRead("0100"))

print(toPinyin("1231"))
print(toPinyin("120100031"))
print(toPinyin("1012000020"))
