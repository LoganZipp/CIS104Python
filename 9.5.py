name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter = dict()

for line in handle :
    line = line.rstrip()
    words = line.split()
    if line.startswith("From:"):
        email = words[1]
        pos = email.find('@')
        address = email[pos+1:]
        counter[address] = counter.get(address, 0) + 1

print(counter)
