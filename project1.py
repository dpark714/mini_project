#Number gussesing game

import random  #importing random modules

userNum = input("Enter a number: ")

if userNum.isdigit(): 
  userNum = int(userNum)

  if userNum <= 0:
    print("Enter a number larger than 0.")
    quit()

else: 
  print("Invalid. Enter a number.")
  
random_number = random.randint(0, userNum) #0 to userNum
guesses = 0

while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit(): 
    user_guess = int(user_guess)
    

  else: 
    print("Invalid. Enter a number.") 
    continue # bring us back to the top of our loop

  if user_guess == random_number:
    print("Correct")
    break

  elif user_guess > random_number:
    print("You were above the number.")
    
  else:
      print("You were below the number.")

print("You got it in", guesses, "guesses.")

    
