'''
Write a program in Python to perform the following operator based task:

● Ask user to choose the following option first:

○ If User Enter 1 - Addition
○ If User Enter 2 - Subtraction
○ If User Enter 3 - Division
○ If USer Enter 4 - Multiplication
○ If User Enter 5 - Average
● Ask user to enter the 2 numbers in a variable for first and second for the
first 4 options mentioned above.
● Ask user to enter two more numbers as first and second2 for
calculating the average as soon as user choose an option 5.
● At the end if the answer of any operation is Negative print a statement
saying “NEGATIVE”
● NOTE: At a time user can perform one action at a time.
'''

##num1 = int(input("Enter First Number: "))
while True:
    try:
        num1 = int(input('Enter First Number: '))
        if num1 < 1 or num1 > 5:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-5.")
if num1 == 1:
    num2 = int(input("Enter Second Number: "))
    result = num1 + num2
    if result < 0:
     print ("NEGATIVE")
if num1 == 2:
    num2 = int(input("Enter Second Number: "))
    result = num1 - num2
    if result < 0:
        print ("NEGATIVE")
if num1 == 3:
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    if result < 0:
        print ("NEGATIVE")
if num1 == 4:
    num2 = int(input("Enter Second Number: "))
    result == num1 * num2
    if result < 0:
        print ("NEGATIVE")
if num1 == 5:
    num2 = int(input("Enter Second Number: "))
    num3 = int(input("Enter Third Number: "))
    result = (num2 + num3) / 2
    #print (result)
    if result < 0:
        print ("NEGATIVE")
        

