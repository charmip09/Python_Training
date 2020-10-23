'''TASK SIX: HIGHER ORDER FUNCTIONS, GENERATORS, LIST
COMPREHENSION AND DECORATOR'''
'''Question 1- Write a program to Python find the values which is not divisible 3 but is should be
a multiple of 7. Make sure to use only higher order function. '''
numbers = range(200)
Result = filter(lambda num: num % 3 != 0 and num % 7 ==0 , numbers)
print(list(Result))

'''QUESTION 2- Write a program in Python to multiple the element of list by itself using a
traditional function and pass the function to map to complete the operation. '''
Num = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*x , Num)) 
print(final_list)

'''QUESTIONS 3- Write a program to Python find out the character in a string which is uppercase
using list comprehension.'''
Full_string = "WorkIsAwesomeButHectic"
print("The original string is : " + str(Full_string)) 
res = [char for char in Full_string if char.isupper()] 
print("The uppercase characters in string are : " + str(res))

'''QUESTION 4- Write a program to construct a dictionary from the two lists containing the names
of students and their corresponding subjects. The dictionary should maps the
students with their respective subjects. Let’s see how to do this using for loops and
dictionary comprehension. '''
Student = ['Charmi','Gauri','Sam']
Subjects = ['Python', 'Java', 'Django'] 

print ("Original key list is : " + str(Student)) 
print ("Original value list is : " + str(Subjects)) 

res = dict(zip(Student, Subjects)) 
print ("Final Dictionary : " +  str(res)) 

'''QUESTION 5- Learn More about Yield, next and Generators'''
DONE

'''QUESTION 6- Write a program in Python using generators to reverse the string. Input String =
"Consultadd Training" '''
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for char in rev_str("Consultadd Training"):
    print(char)

'''QUESTION 7- Write any example on decorators. '''
def decor(func):
  def wrap():
    print("before fun")
    func()
    print("After fun")
  return wrap
def sayhello():
        print("Hello")
newfunc=decor(sayhello)
newfunc()

''' QUESTION 8- Learn about What is FRONT END and its Technologies and Tools
● Make sure to mention at least 5 top notch technologies of Frontend.
● Also mentioned the name of companies using those 5 technologies
individually ''''

1) ReactJS - Pintrest, Netflix and Dropbox
2) Angular JS- Used by BMW, FORBES, XBOX
3) JavaScript- Microsoft, Paypal, UBER
4) Node JS- Capital One, Linkedin
5) VUE.JS- Apple, Nintendo, Trivago