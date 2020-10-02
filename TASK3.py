''' QUESTION1 -
Create a list of the 10 elements of four different types of Data Type like int,
string, complex and float.
'''
a = [ 1, "Charmi", 2.5, 1j, "CONSULTADD", 30, "Patel", 4j, 100, 30.75]
print (a)

''' QUESTION2 -
Create a list of size 5 and execute the slicing structure
'''
a = [ 1, "Charmi", 2.5, 1j, "CONSULTADD", 30, "Patel", 4j, 100, 30.75]*5
a=[1:10]

''' QUSETION3 -
Write a program to get the sum and multiply of all the items in a given list.
'''
import numpy
list1 = [20,30,44,57]
result1 = numpy.prod(list1)
result2 = numpy.sum(list1)
print(result1)
print(result2)

''' QUESTION4 -
Find the largest and smallest number from a given list.
'''
a= [1,22,45,78,100,1000]
print("Smallest number in list :", min(a))
print("Largest number in list :", max(a))

''' QUESTION5-
Create a new list which contains the specified numbers after removing the
even numbers from a predefined list.'''
a = [20,30,31,41,70,80,51,71]
a = [x for x in a if x%2 !=0]
print(a)

''' QUESTION6-
Create a list of first and last 5 elements where the values are square of
numbers between 1 and30 (both included). '''
l=[]
for i in range(1,30):
    l.append(i**2)
print(l[:5])
print(l[-5:])

''' QUESTION7 - Write a program to replace the last element in a list with another list. '''
a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]
a.pop() # get rid of last element
a.extend(b) # extend list a with b data
print(a)

''' QUESTION8 - Create a new dictionary by concatenating the following two dictionaries:'''
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print('Updated dictionary :')
print(a)

''' QUESTION9 - Create a dictionary that contains a number (between 1 and n) in the
form(x,x*x).'''
N=5
myDict = {x:x * x for x in range(1, N + 1)}

print("\nDictionary = ", myDict)

''' QUESTION10 - Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number. Suppose
the following input is supplied to the program: '''

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

''' QUESTION11- QUESTION12 --- BOTH ARE DUPLICATE OF 1&2 '''
'''QUESTION13 -- Create a list of given structure and run '''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
a) Access list [1, 2, 3, 4]
print(x[5][0:4])

b) Access list [600, 700]
print(x[-3:-1])

c) Access list [100, 300, 500, 600, 800]
print(x[0::2])

d) Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300,
200, 100]]
print(x[::-1])

e) Access list [10]
print(x[-4][5][0])

f) Access list [ ]
print(x[-1:-3])

'''QUESTION14 -- Create a list of thousand number using range and xrange and see the difference
between each other. '''
for i in range(1001):
   print(i)
Xrange is not used in version 3 anymore

'''QUESTION15- How Tuple is beneficial as compare to the list? '''
Tuple is more faster as compare to list because its static in nature

'''QUESTION16- Write a program in Python to iterate through the list of numbers in the range of 1,100
and print the number which is divisible by 3 and a multiple of 2. ''''
for i in range(1, 100):
   if((i%3==0) & (i%2==0)):
      print(i)


'''QUESTION17- Write a program in Python to reverse a string and print only the vowel alphabet if
exist in the string with their index. '''
def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
name = input("Enter a word: ")
print(reverse_vowels(name))


'''QUESTION18- Write a program in Python to iterate through the string “hello my name is abcde” and
print the string which has even length of word. '''

def printword(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
s = "hello my name is abcde"
printword(s)

'''QUESTION19- Write a program in python to print the pair of numbers whose sum is equal to result
number that is let&#39;s say 8.

x=[1,2,3,4,5,6,7,8,9,-1]'''
def findPairs(a,b):  
    res = [] 
    while a: 
        num = a.pop() 
        diff = b - num 
        if diff in a: 
            res.append((diff, num)) 
          
    return res 
      
a = [1,2,3,4,5,6,7,8,9,-1]
b = 8
print(findPairs(a, b))

'''QUESTION10. Write a program in Python to complete the following task:'''
evenlist = [] 
oddlist = [] 
counter = 1
while counter <= 50:
 counter = counter +1
 number = int(input("Enter a number: "))
 if (number%2 == 0):
        evenlist.append(number)
        if len(evenlist) == 5:
          break
 else:
        oddlist.append(number)
        if len(oddlist) == 5:
          break
print("Sum of Even lists:", sum(evenlist)) 
print ("Max of the Even list",max(evenlist))
print("Sum of Odd lists:", sum(oddlist)) 
print ("Max of the Odd list",max(oddlist))

''' QUESTION20 Write a program to find out the occurrence of a specific word from an alphanumeric
statement. Example: 12abcbacbaba344ab '''
def Result(str1):
    dict = {}
    str1 = ''.join([i for i in str1 if not i.isdigit()])
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(Result('12abcbacbaba344ab'))

''' QUESTION21 Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10). '''

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)
