# WHAT THIS FILE TEACHES: input() and type()
# input("...") ALWAYS gives back text (str), even when the user types digits.
# type() tells us which data type a value has: str, int, float or bool.
#
# DRY RUN (pretend the user typed the name Amit and the height 170)
#   name   = input(...)   -> name   = 'Amit'  (str)
#   age    = 18           -> age    = 18      (int)
#   height = input(...)   -> height = '170'   (str - NOT a number!)
#   Stud   = True         -> Stud   = True    (bool)
#   print(type(name))     -> <class 'str'>
#   print(type(age))      -> <class 'int'>
#   print(type(height))   -> <class 'str'>
#   print(type(Stud))     -> <class 'bool'>

# Ask the user for their name. input() shows the message, waits for the typing,
# and stores the typed text in the variable "name".
name = input("What is your name :")

# A number written straight into the code (no quotes) is a real number, so age is int.
age = 18

# Same input() as the name line above: whatever the user types lands in "height" as TEXT.
# So typing 170 stores the string '170', and it cannot be used in maths yet.
height = input("How tall are you in (CM):")

# True and False are the two boolean values (bool). Note the capital T / F.
Stud = True

# print(type(name)) -> <class 'str'>, because input() returned text.
print(type(name))

# print(type(age)) -> <class 'int'>, because 18 was written without quotes.
print(type(age))

# print(type(height)) -> <class 'str'>, even though 170 looks like a number.
# To do maths with it you would first write: height = int(height)
print(type(height))

# print(type(Stud)) -> <class 'bool'>, because the value stored is True.
print(type(Stud))
