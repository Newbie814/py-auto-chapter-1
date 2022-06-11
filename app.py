# name = 'Alice'
# if name == 'Bob':
#     print('Hi Alice')
# print('Done')

# password = 'swordfish'
# if password == 'swordfish':
#     print('Access granted')
# else:
#     print('Wrong password')


# name = 'Matt'
# age = 44
# if name == 'Alice':
#     print('Hi Alice')
# elif age < 12:
#     print('You are not Alice, kiddo')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie')
# else:
#     print('Who are you?')
  

# print('Enter a name.')
# name = input()
# if name != '':
#       print('Thank you.')
# else:
#     print('You did not enter a name.')

# spam = 0
# while spam < 5:
#     print('Hello World')
#     spam = spam + 1

# name = ''
# while name != 'Matt':
#   print('Please type YOUR name.')
#   name = input()
#   if name == '':
#     print('You didn\'t enter anything.')
#   else:
#     print('Thank you!')

    



operating_system = ['Windows', 'Mac', 'Linux']
print(operating_system)

operating_system.append('Android')
print(operating_system)

operating_system.insert(1, 'iOS')
print(operating_system)

number = 20

print(type(number))

var = 'python'
print(var.capitalize())  # Capitalize the first letter


# casefold() converts the string into lowercase

var = 'PYTHON IS AWESOME'
print(var.casefold()) # python is awesome

# center() returns a string centered in a field of a given width

var = 'Python'
print(var.center(20)) #          Python            20 parameter dictates a 20px total field width, second parameter(optional) sets a character to fill the rest of the space. Default is whitespace.


print(var.center(20, 'i')) # iiiiiiiPythoniiiiiii

# count() returns the number of times a specified value occurs in a string
var = 'python is awesome and I am enjoying learning python'
print(var.count('a')) # 4   can also be used to count words
print(var.count('python'))  # 2

# endswith() returns true if the string ends with the specified value
var = 'python is awesome'
print(var.endswith('n')) # false
print(var.endswith('awesome')) # true
print(var.endswith('Awesome')) # false     ---- case sensitive

# find()
var = 'python is awesome'
print(var.find('is')) # 7
print(var.find('h')) # 3
print(var.find('z')) # -1(not found)
print(var.find('e')) # 12 finds first instance of specified string
# can specify a start and end index for the search(optional) - start index is inclusive, end index is exclusive

# isalnum() returns true if all characters in the string are alphanumeric
var = 'python is awesome'
print(var.isalnum()) # false (contains a space)
var = 'pythonisawesome'
print(var.isalnum()) # true

# isalpha() returns true if all characters in the string are in the alphabet
var = 'python is awesome'
print(var.isalpha()) # false (contains a space)
var = 'pythonisawesome'
print(var.isalpha()) # true
var = 'python7'
print(var.isalpha()) # false (contains a number)











