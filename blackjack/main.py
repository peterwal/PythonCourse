import random

end_of_game = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

twoCardsComp = random.sample(cards,2)
twoCardsPlayer = random.sample(cards,2)

def checkBlackJack(twocards):
    score = 0
    for number in twocards:
         score += number
    if(score == 21):
        return True
    else:
        return False

def computeScore(twocards):
    score = 0
    for number in twocards:
         score += number
    return score

print(f"Computer: " , twoCardsComp, " Score: ", computeScore(twoCardsComp))
print(f"Player: " , twoCardsPlayer, " Score: ", computeScore(twoCardsPlayer))

while not end_of_game:
    if(checkBlackJack(twoCardsComp)):
        print("computer wins")
        print("player loses")
        end_of_game = True
        break
    if(checkBlackJack(twoCardsPlayer)):
        print("Player wins")
        end_of_game = True
        break
    end_of_game = True


print("over")