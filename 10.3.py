import string
name = input('Enter file name: ')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.strip()
    for word in words:
        letters = word.split()
        for letter in letters:
            if letter.isalpha():
                counts[letter] = counts.get(letter, 0) + 1
            else : continue

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
