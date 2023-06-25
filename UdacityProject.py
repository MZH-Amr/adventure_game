from time import sleep
from random import choice
# Not importing "time" and "random" since only "sleep" and "choice" are needed

II = "Invalid input"
# Invalid input message


def slowPrint(string, delay=1.5):
    # Print slowly

    print(string)
    # Print the value of the "string" parameter

    try:
        sleep(delay)  # Wait "delay" seconds after the "print" statment
    except TypeError:
        print(f"{II} passed to the delay parameter in slowPrint function")
        # If the value of "delay" is not a number, print an error


def takeInput(choices, question):
    # Take player's input and validate it

    answer = input(f"{question}: ")
    # The question parameter is the question that the player will to be asked

    while answer not in choices:
        print(II)
        answer = input(f"{question}: ")
    else:
        return answer


def replay():
    # Give the player an option to replay

    answer = input("Do you want to play again? Yes [Y] No [N]: ")

    if answer.lower() == "y":
        main()  # Replay the game
    elif answer.lower() == "n":
        slowPrint("Game over")  # End the game
    else:
        print(II)
        replay()


def changeScore(change):
    # Change and print the score

    global score
    # Make the score variable global

    try:
        score += change
        # Change the score
    except TypeError:
        print(f"{II} passed to the change parameter in changeScore variable")
        # If the value of "change" is not a number

    if score < 0:
        slowPrint(f"Your score is {score}")
        slowPrint("Score is too low")
        slowPrint("You lost!")
        replay()
    else:
        slowPrint(f"{change} score point(s)")
        # Print the change in score
        slowPrint(f"Your score is {score}")
        # Print the score


def win():
    # When the player wins
    slowPrint("Congratulations!")
    slowPrint("You win!")


def main():
    # The main function for replaying

    global score
    score = 0
    # The score variable
    """
    The score variable is in the main function so the score resets
    whenever the player replays with the replay function
    """

    if deviceBurning():
        if hungry():
            if animalChase():
                if lights():
                    if insect():
                        if treasureNews():
                            findingTreasure()
    # Execute functions which contain the game senarios


def deviceBurning():
    # When the a device catches on fire

    device = choice(
        [
            "computer",
            "PC",
            "laptop",
            "TV",
        ]
    )
    # Choose a random device
    slowPrint("You are at your house")
    slowPrint(f"But your {device} is on fire")
    answer = takeInput(
        ["1", "2"],
        "Should you use the fire extinguisher [1] "
        "or go get some water from the kitchen [2]?"
    )
    # Take the player's input

    if answer == "1":
        slowPrint("Congratulations!")
        slowPrint("You extinguished the fire")
        changeScore(1)
        # Print the score
        return True
        # To execute the next function
    else:
        slowPrint(f"The {device} is pluged in")
        slowPrint("You made it worse")
        slowPrint("Now your house is on fire")
        slowPrint("You lost!")
        replay()


def hungry():
    # When the player goes outside

    food = choice(
        [
            "sandwich",
            "burger",
            "piece of meat",
            "chicken",
        ]
    )
    # Choose random food
    slowPrint("You go outside")
    slowPrint("But you are hungry")
    answer = takeInput(
        ["1", "2"],
        "Should you buy food for 0.5 score point [1] or steal some food [2]?"
    )
    # Take the player's input

    if answer == "1":
        slowPrint("Okay")
        changeScore(-0.5)
    else:
        slowPrint(f"You stole a {food}")
        slowPrint("But someone saw you and called the police")
        slowPrint(
            f"You have to pay the price of the {food} and a 0.5 points fee")
        changeScore(-1)
    return True
    # To execute the next function


def animalChase():
    # When the animal chases the player

    animal = choice(
        [
            "dog",
            "wolf",
            "fox",
            "animal",
        ]
    )
    # Choose a random animal
    slowPrint(f"A hungry {animal} saw you")
    slowPrint("And it's chasing you")
    answer = takeInput(
        ["1", "2"],
        f"Should you run [1] or kill the {animal} [2]?"
    )

    if answer == "1":
        slowPrint(f"You succesfully ran from the {animal}")
        changeScore(1)
    else:
        slowPrint(f"The {animal} bit you")
        slowPrint("Someone takes you to the hospital")
        changeScore(-1)
    return True
    # To execute the next function


def lights():
    # When the lights

    slowPrint("You are back home")
    slowPrint("But the lights go out")
    answer = takeInput(
        ["1", "2"],
        "Should you fix it [1] or call an electrician to fix it [2]?"
    )

    if answer == "1":
        slowPrint("You got shocked by electric wires")
        slowPrint("You go to the hospital")
        changeScore(-1)
    else:
        slowPrint("The electrician fixed the wires")
        changeScore(1)
    return True
    # To execute the next function


def insect():
    # When the spider approaches

    insect = choice(
        [
            "spider",
            "bee",
            "wasp",
        ]
    )
    # Choose a random insect
    slowPrint(f"A {insect} approaches")
    answer = takeInput(
        ["1", "2"],
        f"Should you kill the {insect} [1] or run away [2]?"
    )

    if answer == "1":
        slowPrint("Okay")
        changeScore(1)
    else:
        slowPrint("Really?")
        slowPrint("You should be ashamed!")
        changeScore(-1)
    return True
    # To execute the next function


def treasureNews():
    slowPrint("You sit and watch the TV")
    slowPrint(
        "The news say there is a treasure hidden somewhere"
        " that contains alot of score points"
    )
    answer = takeInput(
        ["1", "2", "3"],
        "Should you search for the treasure [1] or stay home [2]?"
    )

    if answer == "1":
        slowPrint("Okay")
        return True
        # To execute the next function
    elif answer == "2":
        slowPrint("C'mon")
        slowPrint("Find the treasure!")
        return True
        # To execute the next function
    elif answer == "3":
        slowPrint("You found a cheat code")
        win()


def findingTreasure():
    slowPrint("You go outside again")
    slowPrint(
        "Then you enter an old man's house"
        " who claimed that there was a hidden treasure before"
    )
    slowPrint("But no one believed him then")
    slowPrint("So you ask him where is the treasure")
    slowPrint("So he gives you a map")
    slowPrint("You follow the map")
    slowPrint("And you find the treasure")
    changeScore(10)
    win()


main()
