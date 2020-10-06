''' TASK FOUR: FUNCTIONS '''
''' QUESTION1- Write a program to reverse a string '''
def my_function(x):
  return x[::-1]

text = my_function("1234abcd")

print(text)

''' QUESTION2- Write a function that accepts a string and calculate the number of uppercase letters
and lowercase letters. '''

def Word(x):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in x:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", x)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

Word('This is Awesome Game')

'''QUESTION3- Create a function that takes a list and returns a new list with unique elements of the
first list. '''
def unique_list(y):
  x = []
  for a in y:
    if a not in x:
      x.append(a)
  return x

print(unique_list([3,3,3,3,4,5,5,5,5,8,1])) 

'''QUESTION4- Write a program that accepts a hyphen-separated sequence of words as input and
prints the words in a hyphen-separated sequence after sorting them alphabetically. '''
friends='charmi-sandip-romit-swarna-gauri'
 
items=[n for n in friends.split('-')]
items.sort()
print('-'.join(items))

'''QUESTION5- Write a program that accepts a sequence of lines as input and prints the lines after
making all characters in the sentence capitalized. '''

lines = []
while True:
    x = input()
    if x:
        lines.append(x.upper())
    else:
        break

for x in lines:
    print(x)

'''QUESTION6- Define a function that can receive two integral numbers in string form and compute
their sum and print it in console. '''
def calculateSum (a,b):
	s = int(a) + int(b)
	return s 
num1 = "2000"
num2 = "3300"
sum = calculateSum (num1, num2)
print("Sum = ", sum)

'''QUESTION7- Define a function that can accept two strings as input and print the string with
maximum length in console. If two strings have the same length, then the function should
print all strings line by line. '''
string1 = input("")
string2 = input("")
count1 = 0
count2 = 0
for i in string1:
      count1 = count1 + 1

for j in string2:
      count2 = count2 + 1

if (count1 < count2):
      print (string2)

elif (count1 == count2):
      print (string1)
      print (string2)
else:
      print (string1)

'''QUESTION8- Define a function which can generate and print a tuple where the value are square of
numbers between 1 and 20.'''
def numbers():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print("Result: ",tuple(l))
		
numbers()

'''QUESTION9- Write a function called showNumbers that takes a parameter called limit. It should
print all the numbers between 0 and limit with a label to identify the even and odd numbers. '''
def showNumbers(limit):

    for i in range(0,limit +1):
     if i % 2 == 0:
        print(str(i) + ":" +'EVEN')
    else:
        print(str(i) + ":"+ 'ODD')


limit = int(input())

showNumbers(limit)

''' QUESTION10- Write a program which can filter() to make a list whose elements are even number
between 1 and 20 ( both included) '''
ls1 = range(1,21) 
  
is_even = lambda x: x % 2 == 0
ls2 = list(filter(is_even, ls1)) 
  
print(ls2)

''' QUESTION11- Write a program which can map() and filter() to make a list whose elements are
square of even number in [1,2,3,4,5,6,7,8,9,10] '''
num = [1,2,3,4,5,6,7,8,9,10]
 
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, num))
 
print(eve_num)

''' QUESTION12- Write a function to compute 5/0 and use try/except to catch the exceptions '''
def divide (x, y):
  try:
     result = x // y
  except:
     print("Error dividing by zero")

divide(5, 0) 

'''QUESTION13- Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce '''
import operator
from functools import reduce

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
finallst = reduce(operator.add, lists)

print(finallst) 

'''QUESTION14- What is the output of the following codes: '''
def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)

output = 2

def a():
   try:
      f(x, 4)
   finally:
     print('after f')

   print('after f?')
   
a()

output- after f

