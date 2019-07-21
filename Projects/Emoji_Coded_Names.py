# =============================================
# Title:  Emoji Coded Name
# Author: HarishBalaji ShanmugaSundaram
# Date:   22 July 2019
# =============================================
my_dictionary = {}
my_dictionary = {'a': '😊', 'b': '❤️', 'c': '🌴', 'd': '🌻', 'e': '😄',
                 'f': '😍', 'g': '🌸', 'h': '💕', 'i': '🍒', 'j': '😘',
                 'k': '💝', 'l': '☀️', 'm': '🌺', 'n': '💗', 'o': '🍿',
                 'p': '🌞', 'q': '🌈', 'r': '💋', 's': '💎', 't': '👗',
                 'u': '😚', 'v': '😌', 'w': '🌵', 'x': '💐', 'y': '🌼', 'z': '🐾'}
name = input('Enter the Name: \n')
length = len(name)
for x in range(0, length):
    print(my_dictionary[name[x]], end='')
print('')