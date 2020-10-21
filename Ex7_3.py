count = 0
fn = input("Enter file name:")
if fn == "na na boo boo":
    print("Enjoy your cadbury egg, sucker.")
    quit()
try:
    fh = open(fn)
except:
    print("That file doesn't exist")
    quit()
for line in fh:
    count = count + 1
print("There are", count, "lines in", fn)
