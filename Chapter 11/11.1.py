import re
regex = input('Enter Regular Expression: ')
fhandle = open("mbox-short.txt")
count = 0
for line in fhandle:
    x = re.findall(regex, line)
    if len(x) > 0:
        count = count + 1

print('The expression was found', count, 'times')
