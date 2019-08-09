# =================================================
# Title:  Generating Anagrams of the Supplied Word
# Author: HarishBalaji ShanmugaSundaram
# Date:   09 August 2019
# =================================================

from itertools import permutations
import enchant

d = enchant.Dict("en_US")
word = input("Enter a Word: ")

# Generates all the possible arrangements of the letters in the supplied word
L=list(word)
perm=permutations(L)
mylist =[]

# Checks each arrangement against English dictionary
for i in list(perm):
    wow=''.join(i)
    result=d.check(wow)
    if(result == True):
        mylist.append(wow)
        mylist = list(dict.fromkeys(mylist))

# Display non-duplicate entries
length=len(mylist)
for j in range(length):
    print(mylist[j])