# Program: Find a number between 1 and 30
# author: Saul DLD

import random

number_to_guess = random.randint(1, 30)
attempts_log = []
found = False


def main():
    global found
    print_start()

    while not found:
        user_input = input("> Guess the number:")

        if user_input == "exit":
            print_exit(number_to_guess)
            write_log(False)
            break

        attempts_log.append(user_input)

        if user_input.isnumeric():
            user_input = int(user_input)
            if 30 >= user_input >= 1:
                if user_input == number_to_guess:
                    found = True
                    write_log(found)
                    print_success_game()
                else:
                    print(process_input(user_input))
            else:
                print("Number should be in range [1-30]")
        else:
            print("Ups! the input is not a number, try again")


def process_input(number):
    dif = number_to_guess - number
    dif = dif * -1 if (dif < 0) else dif

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
    print("\n======================[START GAME]===========================")
    print("## Try to guess a number between 1 and 30")
    print("## I will tell you if you're: Too far, far or close")
    print("## The game ends when you guess the number or type 'exit'.")
    print("==============================================================")


def print_exit(number):
    print("You give up, number to guess was: {number}".format(number=number))
    print("===========[END OF GAME]==============")


def print_success_game():
    print("You win!!! you guess the number")
    print("GuessingSteps.txt")
    print("===========[END OF GAME]==============")


def write_log(success):
    file = open("GuessingSteps.txt", "w+")
    file.write("===========[START]==============\n")

    for idx, number in enumerate(attempts_log, start=1):
        file.write("Attempt {idx}:  {value} \n".format(idx=idx, value=number))

    if success:
        file.write("You win, you guess the number")
    else:
        file.write("You give up, number to guess was : {number}\n".format(number=number_to_guess))

    file.write("===========[END OF GAME]==============\n")
    file.close()


if __name__ == "__main__":
    main()
