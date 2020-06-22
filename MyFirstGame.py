# The objective of this game is to answer the questions correctly and get 50 points!

ans_1 = "Rice"
ans_2 = "Honda"
ans_3 = "Green"
ans_4 = "1975"
points = 50
counter = 0


print("\n")
print("The objective of this game is to answer the questions correctly and get 50 points! \nAre you ready? Let's go!")
print("\n")

# Question One
question_1 = input("Question 1: What is mummy's favorite food? ")

if question_1.lower() == ans_1.lower():
    print("Correct, you get 20 points!")
    counter = counter + 20
else:
    print("Wrong answer, you get 0 points!")

# Question Two
print("\n")
question_2 = input("Question 2: What is mummy's favorite car? ")

if question_2.lower() == ans_2.lower():
    print("Correct, you get 20 points!")
    counter = counter + 20
else:
    print("Wrong answer, you get 0 points!")

# Question Three
print("\n")
question_3 = input("Question 3: What is mummy's favorite color? ")

if question_3.lower() == ans_3.lower():
    print("Correct, you get 10 points!")
    counter = counter + 20
else:
    print("Wrong answer, you get 0 points!")

# Bonus Question
print("\n")
question_4 = input("Bonus Question: What year was mummy born? ")

if question_4.lower() == ans_4.lower():
    print("Correct, you get 50 bonus points!")
    counter = counter + 50
else:
    print("Wrong answer, you get 0 points!")

print("\n")
if counter >= points:
    print("Congratulations, you are a rock star. You scored " + str(counter) + ".")
else:
    print("Better luck next time, boomer :(. You scored " + str(counter) + ".")

# End of code





