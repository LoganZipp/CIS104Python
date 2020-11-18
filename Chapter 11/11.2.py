import re
fhandle = open("mbox-short.txt")
lst = list()
for line in fhandle:
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        for n in x:
            lst.append(int(n))

print(int(sum(lst) / len(lst)))
