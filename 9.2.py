name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter = dict()

for line in handle :
    line = line.rstrip()
    words = line.split()
    if line.startswith("From "):
        day = words[2]
        counter[day] = counter.get(day, 0) + 1

print(counter)
