'''
In the previous question, insert “break” after the “Good guess!” print statement.
“break” will terminate the while loop so that users do not have to continue guessing
after they found the number. If the user does not guess the number at all, print
“Sorry but that was not very successful”.
'''
counter = 0
while counter <= 4:
 counter = counter +1
 number = int(input("Guess the " + str(counter) + ". number "))
 if number != 5:
        print("Try again.")
 else:
        print("Good guess!")
        break
if counter == 5:
   print("Game over")
else:
    print("Sorry but that was not very successful")