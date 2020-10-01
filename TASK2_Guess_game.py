'''
Write a program such that it asks users to “guess the lucky number”. If the
correct number is guessed the program stops, otherwise it continues forever.
'''
number = int(input("Guess the lucky number "))
while number != 5:
   print("That is not the lucky number")
   number = int(input("Guess the lucky number "))
if number == 5:
    print("You guessed it right")
'''
Modify the program so that it asks users whether they want to guess again
each time. Use two variables, ‘number’ for the number and ‘answer’ for the
answer to the question whether they want to continue guessing. The
program stops if the user guesses the correct number or answers “no”. ( The
program continues as long as a user has not answered “no” and has not
guessed the correct number)
'''
number = -1
again = "yes"
while number != 5 and again != "no":
        number = input("Guess the lucky number: ")
        if number != 5:
          print("That is not the lucky number")
          again = input("Would you like to guess again? ")
   

    