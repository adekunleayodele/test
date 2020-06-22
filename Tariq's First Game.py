ans_1 = "Jolly Ranchers"
ans_2 = "Chocolate Chip Cookie Dough"
ans_3 = "Fortnite"
player_ans = ""
score = 0
print("The objective of the game is to try and guess what my favorites things are.")
#print("\n 1. What is my favorite candy? ")
player_ans = input("\n\n\nWhat is my favorite candy? ")
if player_ans.lower() == ans_1.lower():
    print("Correct! You get 20 points!")
    score = score + 20
else:
    print("Wrong! You get 0 points.")
player_ans = input("\n\n\nWhat is my favorite Ice cream flavor? ")
if player_ans.lower() == ans_2.lower():
    print("Correct! You get 20 points!")
    score = score + 20
else:
    print("Wrong! You get 0 points.")
player_ans = input("\n\n\nWhat is my favorite game? ")
if player_ans.lower() == ans_3.lower():
    print("Correct! You get 20 points!")
    score = score + 20
else:
    print("Wrong! You get 0 points.")

if score >= 60 :
    print("\n\n\nCongratulations, you are a  star pickle! You scored " + str(score) + ".")
else:
    print("\n\n\nBetter luck next time, banana :(. You scored "+ str(score) + ".")