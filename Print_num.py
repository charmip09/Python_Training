'''
Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
'''

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
