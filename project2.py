#Ask users questions, we add the score if users get the right answer

#Quiz game

print("Welcome to quiz!")

playing = input("Do you want to play game? ")

if playing.lower() != "yes":
  quit()

print("Great! Let's get started!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct")
  score += 1
else: 
  print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("Correct")
  score +=1
else: 
  print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct")
  score +=1
else: 
  print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
  print("Correct")
  score +=1
else: 
  print("Incorrect")

print("You got ", score, "questions correct")
print("You got ", (score/4)*100, "% correct")

