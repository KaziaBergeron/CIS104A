import string

count = 0
letters = dict()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words :
        for letter in word :
            count += 1
            if letter not in letters :
                letters[letter] = 1
            else :
                letters[letter] += 1

lst = list()
for key, val in list(letters.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
