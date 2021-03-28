# Implement custom functions for str() and int()
# author: Saul DLD

def main():
    int_numbers = [1]
    str_numbers = ["1"]

    print("\ncustom str() function")
    print_separator()
    for int_n in int_numbers:
        try:
            print_convert_output(int_n)
            str_n = int_to_str(int_n)
            print_convert_output(str_n)
        except Exception as e:
            print(e)

        print_separator()

    print("\ncustom int() function")
    print_separator()
    for str_n in str_numbers:
        try:
            print_convert_output(str_n)
            int_n = str_to_int(str_n)
            print_convert_output(int_n)
        except Exception as e:
            print(e)

        print_separator()


# --------------------------------------------------------
# Custom implementation of the str() function
# --------------------------------------------------------
def int_to_str(int_number):
    if int_number == 0:
        return "0"

    # 1 calculate place value
    current_divisor = 1

    while True:
        quotient = int(int_number / current_divisor)
        if quotient == 0:
            break

        divisor = current_divisor
        current_divisor *= 10

    # 2 make divisions until divisor is 1
    str_number = ""
    dividend = int_number
    while True:
        if divisor == 0:
            break

        div_mod = divmod(dividend, divisor)
        str_number += get_str(div_mod[0])  # "1234...."
        dividend = div_mod[1]
        divisor = int(divisor / 10)

    return str_number


# --------------------------------------------------------
# Custom implementation of the int() function
# --------------------------------------------------------
def str_to_int(str_number):
    str_number = prepare_str(str_number)
    sign = str_number[0]
    new_str = str_number[1]

    num_len = len(new_str) - 1
    final_number = 0

    for n in new_str:
        num = get_int(n)
        place_value = 10 ** num_len
        temp = num * place_value
        final_number += temp
        num_len = num_len - 1

    return final_number * sign


# Validate only first symbol
def prepare_str(str_number):
    sign = 1
    if str_number[0] == "-":
        sign = -1
        str_number = str_number.replace("-", "", 1)

    elif str_number[0] == "+":
        str_number = str_number.replace("+", "", 1)

    return [sign, str_number]


def get_int(n):
    if n == "0":
        integer = 0
    elif n == "1":
        integer = 1
    elif n == "2":
        integer = 2
    elif n == "3":
        integer = 3
    elif n == "4":
        integer = 4
    elif n == "5":
        integer = 5
    elif n == "6":
        integer = 6
    elif n == "7":
        integer = 7
    elif n == "8":
        integer = 8
    elif n == "9":
        integer = 9
    else:
        raise Exception("Unable to convert number")

    return integer


def get_str(n):
    if n == 0:
        str_number = "0"
    elif n == 1:
        str_number = "1"
    elif n == 2:
        str_number = "2"
    elif n == 3:
        str_number = "3"
    elif n == 4:
        str_number = "4"
    elif n == 5:
        str_number = "5"
    elif n == 6:
        str_number = "6"
    elif n == 7:
        str_number = "7"
    elif n == 8:
        str_number = "8"
    elif n == 9:
        str_number = "9"
    else:
        raise Exception("Unable to convert number")

    return str_number


def print_separator():
    print("-" * 50)


def print_convert_output(number):
    print("{type} : {number}".format(type=type(number), number=number))


if __name__ == "__main__":
    main()
