# =============================================
# Title:  Reversing A String
# Author: HarishBalaji ShanmugaSundaram
# Date:   22 July 2019
# =============================================
name1    = input("Enter Any Name")
length1 = len(name1)
y = len(name1)-1
x = 0

print('Supplied Text:')
while(x < length1):
        print(name1[x], end='')
        x = x+1
print('')

print('Reversed Text:')
while(y >= 0):
        print(name1[y], end='')
        y=y-1
print('')
