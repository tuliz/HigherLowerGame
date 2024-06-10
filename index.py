#create dictionary for poeple and import
from data import people
from random import choice

#get a random person for comparison A and get a random person for comparison B
def randomChoice(people):
    """get a random people from dictionary. returns that random choice."""
    rand = choice(people)
    return rand

def isHigher(playerChoice, comparison):
    """sends the choice of the player and compare the followers number for both and send true or false"""
    if playerChoice["followerCount"] > comparison["followerCount"]:
        return True
    else:
        return False

def formatData(comparison):
    return f"{comparison["name"]}, a {comparison["description"]}, from {comparison["country"]}\n"

def game():

    gameContinue = True

    #initialise a score
    score = 0
    comparisonA = randomChoice(people)
    comparisonB = randomChoice(people)
    if comparisonA == comparisonB:
        comparisonB = randomChoice(people)

    #looping trough game when the guess is correct
    while gameContinue:

        print(f"Compare A: {formatData(comparisonA)}")
        print("VS\n")
        print(f"Against B: {formatData(comparisonB)}")

        answer = input("Who has more followers? Type 'a' or 'b': ").lower()

        if answer == 'a':
            playerChoice = comparisonA
            comparison = comparisonB

        elif answer == 'b':
            playerChoice = comparisonB
            comparison = comparisonA

            if comparisonA == comparisonB:
                comparisonB = randomChoice(people)
    
    #check choice of player if the choice he chose has a higher follower count then the other choice
    #if the choice is right up the score by one and get a new random preson for comparison B and put the right choice in comparison A
        if isHigher(playerChoice=playerChoice, comparison=comparison):
            score+=1
            print(f"You are right! Current Score: {score}")
            comparisonA = playerChoice
            comparisonB = randomChoice(people)
            
    #if not right end the game
        else:
            print(f"Game Over. Your Final Score is: {score}")
            return


#start game
game()