
import re

import matplotlib.pyplot as plt
import matplotlib
""""

"""




path=r"C:\Users\Ahri\Downloads\taskmanager.log"


pattern="""(?P<dt>\d{4}.*) INFO  org\.apache\.flink\.runtime\.taskexecutor\.TaskManagerRunner      \[\] - Memory usage stats: \[HEAP: (?P<used>\d+)/(?P<committed>\d+)/(?P<max>\d+) MB, NON HEAP: (?P<used2>\d+)/(?P<committed2>\d+)/(?P<max2>\d+) MB \(used/committed/max\)\]"""
regex=re.compile(pattern)

memory=[]
with open(path,"r",encoding="utf-8") as f:
    count=0
    while True:
        line=f.readline()
        if not line:
            break

        if "org.apache.flink.runtime.taskexecutor.TaskManagerRunner" not in line:
            continue
        res=regex.search(line)
        if not res:
            continue
        # groups=res.groups()
        # import ipdb;ipdb.set_trace()
        count+=1
        memory.append((count,int(res.group("used")),int(res.group("committed")),int(res.group("max"))))

print("Memory Set Len:",len(memory))
dataset= list(zip(*memory))



print(dataset[0])
print(dataset[1])

# plt.plot(dataset[0],dataset[1])
plt.figure(figsize=(100,20),dpi=80)
plt.plot(dataset[0],dataset[1])


plt.show()
