from itertools import permutations
import enchant

d = enchant.Dict("en_US")
word = input("Enter a Word: ")

L=list(word)
perm=permutations(L)
mylist =[]

for i in list(perm):
    wow=''.join(i)
    result=d.check(wow)
    if(result == True):
        mylist.append(wow)
        mylist = list(dict.fromkeys(mylist))

length=len(mylist)
for j in range(length):
    print(mylist[j])