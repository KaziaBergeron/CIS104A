fname = input("Enter file name: ")
if fname == 'na na boo boo' :
    print('NA NA BOO BOO TO YOU - You have been punk'+'\''+'d')
    exit()
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
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
