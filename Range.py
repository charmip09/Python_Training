'''
Write a program in Python which will find all such numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200.
'''

print(*[x for x in range(2000, 3201) if not(x%7) and x%5])


