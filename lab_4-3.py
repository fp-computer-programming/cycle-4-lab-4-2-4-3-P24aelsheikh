""""
Write a program that contains a conditional similar to that on slide 4 that will compare two strings 
provided by the user and return if the strings are equal, one string is greater than the other, or one string is less than the other.
"""
word='fruit'
if word == "pineapple":
    print('pineapple for scale.')
if word < 'pineapple':
    print(word + 'comes before pineapple')
elif word > 'pineapple':
    print(word + 'comes after pineapple')
else:
    print('pineapple for scale.')