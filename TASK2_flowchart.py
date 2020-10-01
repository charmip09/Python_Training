##Write a program in Python to implement the given flowchart:

a = 10
b = 20
c = 30

Avg = (a+b+c)/3
print ("Avg=",Avg)
if (Avg > a and Avg > b and Avg > c):
    print("Avg is higher than a, b, c")
if (Avg > a and Avg > b):
    print("Avg is higher than a,b")
if (Avg > a and Avg > c):
    print("Avg is higher than a,c")
if (Avg > b and Avg > c):
    print("Avg is higher than b,c")
if (Avg > a):
    print("Avg is just higher than a")
if (Avg > b):
    print("Avg is just higher than b")
if (Avg > c):
    print("Avg is just higher than c")