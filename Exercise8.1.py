def chop():
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    letters.remove('a')
    letters.remove('f')
    print(letters)

chop()

letters = ['a', 'b', 'c', 'd', 'e', 'f']
def middle(letters):
    return letters[1:5]

newlist = middle(letters)
print(newlist)
