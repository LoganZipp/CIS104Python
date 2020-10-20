# Use the file name mbox-short.txt as the file name
total = 0
count = 0
fname = input("Enter file name: ")

fh = open(fname)

for line in fh:
	if line.startswith("X-DSPAM-Confidence:"):
		pos = line.find(":")
		number = line[pos+1:]
		total = total + float(number)
		count = count + 1


avg = total/count
print("Average spam confidence:", avg)
