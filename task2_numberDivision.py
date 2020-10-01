'''
Write a program in Python to perform the following operation:

● If a number is divisible by 3 it should print “Consultadd” as a string
● If a number is divisible by 5 it should print “c” as a string
● If a number is divisible by both 3 and 5 it should print “Consultadd
Python Training” as a string.
'''

number = int(input(" Please Enter any Number : "))
if (number % 3 == 0):
    print("Consultadd")
if (number % 5 == 0):
    print("c")
if ((number % 3 == 0) and (number % 5 == 0)):
   print("Consultadd Python Training")

