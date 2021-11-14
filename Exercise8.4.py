fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    line = line.rstrip()
    line = line.split()
    for element in line :
        if element not in lst :
            lst.append(element)
lst.sort()
print(lst)
