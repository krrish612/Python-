# input("...") shows the message in the brackets and then waits for the user to type something.
# Whatever the user types is stored inside the variable "age".
age = input("how old are you:")

# print() shows the value that is stored in the variable "age".
print(age)

# type() tells us what kind of data a value is.
# input() always gives back text, so this prints <class 'str'> (str means string/text),
# even when the user types a number like 20.
print(type(age))