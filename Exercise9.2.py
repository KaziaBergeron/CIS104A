dow = dict()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    words = line.split()
    if len(words) == 0 or len(words) < 3 or words[0] != 'From' :
        continue
    else:
        if words[2] not in dow:
            dow[words[2]] = 1
        else:
            dow[words[2]] += 1
print(dow)
