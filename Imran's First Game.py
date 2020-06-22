# the objective of the game is to try and get all of the questions correctly, and to get 50 points

answer_check = "Fortnite"
answer = ""
points = 50
counter = 0

print("\n")
print("The objective of the game is to try and get all of the questions correctly and get 50 points \n Ready, Set, GO! ")
print("\n")

# Question number 1
#print("What is Imran's favorite video game?")

answer = input("What is Imran's favorite video game? ")
if answer.upper() == answer_check.upper():
    counter = counter + 25
    print("Yay, you got it correct, and you have " + str(counter) + " points")
else:
    print("Sorry, you got that question wrong")
