# Program: Convert decimal number to binary and hexadecimal
# author: Saul DLD

def main():
    exit = False

    while not exit:
        user_input = input("> Number to convert:")

        if user_input == "exit":
            print("Exit program")
            exit = True
        else:
            try:
                user_input = validate_input(user_input)
                print("Binary: ", "".join(convert_2_binary(user_input)))
                print("Hexadecimal:  0x", "".join(convert2Hexa(user_input)))
            except Exception as ex:
                print("Exception: ", ex)


def validate_input(number):
    try:
        number = int(number)
    except Exception as e:
        raise Exception("Input is not a number")

    if number < 0:
        raise Exception("Number should be greater than zero")

    return number


def convert_2_binary(number):
    binary = []
    dividend = number

    while dividend >= 2:
        quotient = int(dividend / 2)
        remainder = int(dividend % 2)
        binary.append(str(remainder))
        dividend = quotient

    binary.append(str(dividend))
    binary.reverse()
    return binary


def convert2Hexa(number):
    hexa = []
    dividend = number

    while dividend >= 16:
        quotient = int(dividend / 16)
        remainder = int(dividend % 16)
        hexa.append(remainder)
        dividend = quotient

    hexa.append(dividend)

    for i in range(len(hexa)):
        if hexa[i] == 10:
            hexa[i] = "A"
        elif hexa[i] == 11:
            hexa[i] = "B"
        elif hexa[i] == 12:
            hexa[i] = "C"
        elif hexa[i] == 13:
            hexa[i] = "D"
        elif hexa[i] == 14:
            hexa[i] = "E"
        elif hexa[i] == 15:
            hexa[i] = "F"
        else:
            hexa[i] = str(hexa[i])

    hexa.reverse()
    return hexa


if __name__ == "__main__":
    main()
