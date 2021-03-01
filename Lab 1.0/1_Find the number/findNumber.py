# Program: Find a number between 1 and 30
# author: Saul DLD

import random

numberToGuess = random.randint(1, 30)
# attemptsCounter = 0
attemptsLog = []
found = False


def main():
    global found
    print_start()

    while not found:
        user_input = input("> Guess the number:")

        # Exit Game by User
        if user_input == "exit":
            print_exit(numberToGuess)
            writeLog(False)
            break

        attemptsLog.append(user_input)

        if user_input.isnumeric():
            user_input = int(user_input)
            if 30 >= user_input >= 1:
                if user_input == numberToGuess:
                    found = True
                    writeLog(found)
                    print_success_game(user_input)
                else:
                    print(processInput(user_input))
            else:
                print("Number should be in range [1-30]")
        else:
            print("Ups! the input is not a number, try again")


def processInput(number):
    dif = numberToGuess - number

    if dif < 0:
        dif = dif * -1

    if dif <= 3:
        msg = "You're too close"
    elif dif <= 8:
        msg = "You're close"
    elif dif <= 15:
        msg = "You're far"
    else:
        msg = "You're too far"

    return msg


def print_start():
    print(" ")
    print("======================[START GAME]===========================")
    print("## Rules:")
    print("## Try to guess a number between 1 and 30")
    print("## I will tell you if you're: Too far, far or close")
    print("## The game ends when you guess the number or type 'exit'.")
    print("==============================================================")
    print(" ")


def print_exit(number):
    print(" ")
    print("===========[END OF GAME]==============")
    print("You give up!")
    print("Number to guess was:", number)
    print("Attempts:", len(attemptsLog))
    print("======================================")
    print(" ")


def print_success_game(number):
    print(" ")
    print("===========[END OF GAME]==============")
    print("You Win!!!!")
    print("Number:", number)
    print("Attempts:", len(attemptsLog))
    print("Results: GuessingSteps.txt")
    print("======================================")
    print(" ")


def writeLog(success):
    file = open("GuessingSteps.txt", "w+")
    file.write("===========[START]==============\n")

    for idx, number in enumerate(attemptsLog, start=1):
        file.write("Attempt {idx}:  {value} \n".format(idx=idx, value=number))

    file.write("-------------------\n")

    if success:
        file.write("You win, you guess the number: {number}\n".format(number=numberToGuess))
    else:
        file.write("You give up, number to guess was : {number}\n".format(number=numberToGuess))

    file.write("===========[END OF GAME]==============\n")
    file.close()


if __name__ == "__main__":
    main()
