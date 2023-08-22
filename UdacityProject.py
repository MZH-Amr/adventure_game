from time import sleep
from random import choice
# Not importing "time" and "random" since only "sleep" and "choice" are needed

II = "Invalid input"
# Invalid input message


def slowPrint(string, delay=1.5):
    """
    Prints the "string" parameter
    then waits "delay" seconds
    """

    print(string)
    # Print the value of the "string" parameter

    try:
        sleep(delay)  # Wait "delay" seconds after the "print" statment
    except TypeError:
        print(f"{II} passed to the delay parameter in slowPrint function")
        # If the value of "delay" is not a number, print an error


def takeInput(choices, question):
    """
    Asks the player by printing the "question" parameter
    then takes the player input and make sure it's in the "choices" parameter
    """

    answer = input(f"{question}: ")
    # The question parameter is the question that the player will to be asked

    while answer not in choices:
        print(II)
        answer = input(f"{question}: ")
    else:
        return answer


def replay():
    """
    Give the player an option to replay
    in the case of a loss
    """

    answer = input("Do you want to play again? Yes [Y] No [N]: ")

    if answer.lower() == "y":
        main()  # Replay the game
    elif answer.lower() == "n":
        slowPrint("Game over")  # End the game
    else:
        print(II)
        replay()


def changeScore(score, change):
    """
    Changes the score then prints it
    then prints by how much the score changed
    and makes sure the score is not less than 0
    """

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
        return score
        # Returns the score so the main function changes it


def win():
    # When the player wins
    slowPrint("Congratulations!")
    slowPrint("You win!")


def main():
    # The main function which executes each senario

    score = 0
    """
    This is the score variable,
    the score variable is in the main function so the score resets
    whenever the player replays
    """

    senarios = [deviceBurning,
                hungry,
                animalChase,
                lights,
                insect,
                treasureNews,
                findingTreasure,
                ]

    for senario in senarios:
        result = senario()
        if result:
            score = changeScore(score, result)
        else:
            replay()


def deviceBurning():
    """
    This is the 1st game senario
    A device catches on fire
    """

    device = choice(
        [
            "computer",
            "PC",
            "laptop",
            "TV",
            "microwave",
            "fan",
        ]
    )
    """
    Chooses a random device
    which will catch fire
    """

    slowPrint("You are at your house")
    slowPrint(f"But your {device} is on fire")
    answer = takeInput(
        ["1", "2"],
        "Should you use the fire extinguisher [1] "
        "or go get some water from the kitchen [2]?"
    )
    # Take the player's choice

    if answer == "1":
        slowPrint("Congratulations!")
        slowPrint("You extinguished the fire")
        return 1
        """
        Returns "1" so the main function
        changes the score by 1
        and executes the next senario
        """
    else:
        slowPrint(f"The {device} was plugged in")
        slowPrint("You made it worse")
        slowPrint("Now your house is on fire")
        slowPrint("You lost!")
        return 0
        """
        Returns "0" so the main function
        gives the player the option to replay
        """


def hungry():
    """
    This is the 2nd game senario
    The player goes outside and get hungry
    """

    food = choice(
        [
            "a sandwich",
            "a burger",
            "a pizza",
            "some meat",
            "chicken",
            "french fries",
        ]
    )
    # Chooses random food

    slowPrint("You go outside")
    slowPrint("But you are hungry")
    answer = takeInput(
        ["1", "2"],
        "Should you buy food for 0.5 score point [1] or steal some food [2]?"
    )
    # Take the player's input

    if answer == "1":
        slowPrint("Okay")
        return -0.5
        """
        Returns "-0.5" so the main function
        changes the score by -0.5
        and executes the next senario
        """
    else:
        slowPrint(f"You stole {food}")
        slowPrint("But someone saw you and called the police")
        slowPrint(
            f"You have to pay the price of the {food} and a 0.5 points fee"
        )
        return -1
        """
        Returns "-1" so the main function
        changes the score by -1
        and executes the next senario
        """


def animalChase():
    """
    This is the 3rd game senario
    An animal chases the player
    """

    animal = choice(
        [
            "dog",
            "wolf",
            "fox",
            "animal",
        ]
    )
    # Chooses a random animal

    slowPrint(f"A hungry {animal} saw you")
    slowPrint("And it's chasing you")
    answer = takeInput(
        ["1", "2"],
        f"Should you run [1] or kill the {animal} [2]?"
    )

    if answer == "1":
        slowPrint(f"You succesfully ran from the {animal}")
        return 1
        # Changes score and executes next senario
    else:
        slowPrint(f"The {animal} bit you")
        slowPrint("Someone takes you to the hospital")
        return -1
        # Changes score and executes next senario


def lights():
    """
    This is the 4th game senario
    The lights go out
    """

    slowPrint("You are back home")
    slowPrint("But the lights go out")
    answer = takeInput(
        ["1", "2"],
        "Should you fix it [1] or call an electrician to fix it [2]?"
    )

    if answer == "1":
        slowPrint("You got shocked by electric wires")
        slowPrint("You go to the hospital")
        return -1
        # Changes score and executes next senario
    else:
        slowPrint("The electrician fixed it")
        return 1
        # Changes score and executes next senario


def insect():
    """
    This is the 5th game senario
    An insect approaches
    """

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
        return 1
        # Changes score and executes next senario
    else:
        slowPrint("Really?")
        slowPrint("You should be ashamed!")
        return -1
        # Changes score and executes next senario


def treasureNews():
    """
    This is the 6th game senario
    The news talk about a treasure
    """

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
        return 0.5
        # Changes score and executes next senario
    elif answer == "2":
        slowPrint("C'mon")
        slowPrint("Find the treasure!")
        return -0.5
        # Changes score and executes next senario
    elif answer == "3":
        slowPrint("You found a cheat code")
        win()
        # A way to win fast...-er, well, it's not that much faster


def findingTreasure():
    """
    This is the 7th and the last game senario
    The player gets the treasure
    """

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
    win()
    # The player wins here


main()
