#  Copyright (c) 2022. Ahri.cool All rights reserved.
import sys
import re
from collections import defaultdict

pattern = "filter_type=(?P<type>\w+)"
regex = re.compile(pattern)

d=defaultdict(int)

def analysis(file_name):
    with open(file_name,encoding="utf-8") as file:
        for line in file.readlines():
            res = regex.search(line)
            if res is not None:
                d[res.group("type")]+=1

    print(d)



if __name__ == "__main__":
    print(sys.argv[1])
    analysis(sys.argv[1])


