fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
count = 0
tot = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: 0.8475") : continue
    count = count + 1
    num = float(line[21:])
    print(line)
print("Done")
