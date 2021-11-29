import re

fname = input("Enter file name: ")
fh = open(fname)
count = list()
for line in fh :
    number = re.findall('[0-9]+',line)
    count = count + number

sum = 0
for num in count :
    sum = sum + int(num)

print(sum)
