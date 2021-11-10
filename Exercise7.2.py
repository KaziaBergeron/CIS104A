fname = input("Enter file name: ")
fh = open(fname)
count = 0
runtotal = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        num = float(line.split(':',1)[1])
        runtotal = num + runtotal
    continue
avg = runtotal / count

print('Average spam confidence:', avg)
