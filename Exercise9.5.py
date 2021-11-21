email = dict()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    else:
        domain = words[1].split("@")
        if domain[1] not in email:
            email[domain[1]] = 1
        else:
            email[domain[1]] += 1

print(email)
