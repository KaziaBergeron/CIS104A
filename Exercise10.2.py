hour = dict()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' :
        continue

    time = words[5].find(':')
    hr = words[5][:time]
    if hr not in hour:
        hour[hr] = 1
    else:
        hour[hr] += 1

lst = list()
for key, val in list(hour.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
