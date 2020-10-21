''' Question1-
Write a program in Python to allow the error of syntax to go in exception.'''
raise SyntaxError("This is my error text")

''' Question2- 
Write a program in Python to allow user to open a file by using argv module. If
the entered name is incorrect throw an exception and ask them to enter the name
again. Make sure to use read only mode. '''
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()
    fh.close()
except IOError:
    print('cannot open', file_name)

''' Question3-
Write a program to handle an error if the user entered the number more than
four digits it should return “Please length is too short/long !!! Please provide only four
digits” '''
while True:
    try:
        a =input("Please enter a Number: ")
        if len(a)>4 or len(a)<4:
            raise ValueError      
    except:
        print("Please length is too short/long!!! Please provide only four digits")
    
    else:
        if a==4:
            print("Number looks good")
            break

''' QUESTION 4-
Create a login page backend to ask user to enter the UserEmail and password.
Make sure to ask Re-Type Password and if the password is incorrect give chance to
enter it again but it should not be more than 3 times. '''

print('Enter correct username and password combination to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Charmi123' and username=='charmip09':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

''' QUESTION 6- 
Read any file using Python File handling concept and return only the even
length string from the doc.txt file.
Consider the content as: '''
x=open("sample.txt", "r")
a=x.read()
words=a.split()
for i in words:
    if len(i) % 2 == 0:
        print(i)