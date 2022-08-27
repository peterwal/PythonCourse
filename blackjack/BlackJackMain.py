import random

end_of_game = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

twoCards = []
cardsComp = []
cardsPlayer = []

def dealcard():
    card = random.choice(cards)
    return card

def checkBlackJack(cards):
    score = 0
    for number in cards:
        score += number
    if(score == 21):
        return True
    else:
        return False

def aceOrNot(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return True
    return False

def computeScore(cards):
    score = 0
    aceOrNot(cards)
    for number in cards:
         score += number
    return score

def checkUser21():
    if (computeScore(cardsPlayer) > 21):
        return True


for _ in range(2):
    cardsComp.append(dealcard())
    cardsPlayer.append(dealcard())

while not end_of_game:
    if(checkBlackJack(cardsComp)):
        print("computer wins")
        print("player loses")
        end_of_game = True
        break
        
    if(checkBlackJack(cardsPlayer)):
        print("Player wins")
        end_of_game = True
        break

    print(f"Player: ", cardsPlayer, " Score: ", computeScore(cardsPlayer))

    print(f"Computer's first card is: ", cardsComp[0]) #show computer's first card
    anotherUsercard = "y"
    while anotherUsercard == "y":
        anotherUsercard = input(f"Would you like another card? y/n: ")
        if(anotherUsercard == "y"):
            cardsPlayer.append(dealcard())
            if (checkUser21() or checkBlackJack(cardsPlayer)):
                anotherUsercard = "n"
                end_of_game = True
            print(f"Player: ", cardsPlayer, " Score: ", computeScore(cardsPlayer))
        else:
            anotherUsercard = "n"
            end_of_game = True


print(f"Computer: ", cardsComp, " Score: ", computeScore(cardsComp))
print(f"Player: ", cardsPlayer, " Score: ", computeScore(cardsPlayer))

print("over")