## OPERATORS IN PYTHON
## -------------------
## An operator is a symbol that performs an action on values (the values are
## called operands). Arithmetic operators make Python work like a calculator.
## There are 7 main arithmetic operators:
##   1) +   addition              10 + 3   -> 13
##   2) -   subtraction           10 - 3   -> 7
##   3) *   multiplication        10 * 3   -> 30
##   4) /   division (float)      10 / 3   -> 3.3333333333333335
##   5) //  floor division        10 // 3  -> 3     (whole part only)
##   6) %   modulus (remainder)   10 % 3   -> 1
##   7) **  power (exponent)      10 ** 3  -> 1000
##
## DRY RUN of this file (each line runs from top to bottom:
## "10 op 3" is worked out first, then print() shows the answer):
##   print(10 + 3)   -> 13
##   print(10 - 3)   -> 7
##   print(10 * 3)   -> 30
##   print(10 - 3)   -> 7    <-- same answer as the subtraction above
##   print(10 // 3)  -> 3    <-- // drops the remainder
##   print(10 % 3)   -> 1    <-- % gives back that remainder
##
## NOTE: this file uses only + - * // % . The / and ** operators are not used yet.

## Addition: add the two numbers together -> 13
print(10 + 3)

## Subtraction: take the second number away from the first -> 7
print(10 - 3)

## Multiplication: 10 added three times (10+10+10) -> 30
print(10 * 3)

## Subtraction again: this line is exactly the same as the subtraction above,
## so it also prints 7. It was probably meant to be print(10 / 3),
## which would print 3.3333333333333335.
print(10 - 3)

## Floor division: divide, then keep only the whole part, so 10 // 3 -> 3
## (the .333... is thrown away, not rounded).
print(10 // 3)

## Modulus: give back the remainder after division.
## 10 % 3 -> 1 because 3 fits into 10 three times (3 * 3 = 9) and 1 is left over.
print(10 % 3)




