word = input("Enter a Word: ")
L = list(word)
print(L)
print(L[::-1])  # Reversed Copy of the List

if (L == L[::-1]):
    print('Palindrome')
else:
    print('Not a Palindrome')
