number_list = []


def greet(message):
    print(message)


def restart_or_not():
    print('Do you want to restart the calculator? \n')
    ask = input('1. Enter Y/y for yes \n2. Enter N/n for no \n')

    if ask == 'Y' or ask == 'y':
        print('Restarted Successfully')
        user_interface()
    else:
        print('Thank you \nStay at your home \nWash your hand \nBe Safe')


# Todo1: User_input

def get_me_numbers():
    global number_list
    print('Enter D/d when Done')
    while True:
        inp = input('Enter number: \n')

        if inp == 'D' or inp == 'd':
            break
        else:
            number_list.append(float(inp))

    print('Numbers are: ', number_list)

    return number_list


def get_me_numbers_for_div():
    global number_list
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    return int(num1), int(num2)


# Todo: user_interface

def user_interface():
    print('Please select an option from below list ')
    print('1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Average')
    option_value = input('Enter option here: ')

    # Todo2: User_input operation

    if int(option_value) == 1:
        numbers = get_me_numbers()
        add = add_numbers(numbers)
        print('Sum of numbers is', add)
        restart_or_not()
    elif int(option_value) == 2:
        numbers = get_me_numbers()
        sub = sub_numbers(numbers)
        print('Difference of numbers is ', sub)
        restart_or_not()
    elif int(option_value) == 3:
        numbers = get_me_numbers()
        mult = multiply_numbers(numbers)
        print('Product of numbers is ', mult)
        restart_or_not()
    elif int(option_value) == 4:
        numbers = get_me_numbers_for_div()
        div = div_numbers(numbers)
        print('div of numbers is ', div)
        restart_or_not()
    elif int(option_value) == 5:
        numbers = get_me_numbers()
        avg = avg_numbers(numbers)
        print('Average of numbers is', avg)
        restart_or_not()
    else:
        print('Please Enter a valid input')
        restart_or_not()


# Todo3: Add

def add_numbers(num):
    ans = 0
    for i in num:
        ans = ans + i

    return ans


# Todo4: sub
def sub_numbers(num):
    ans = 0
    for i in num:
        ans = ans - i

    return ans


# TOdo5: multiply
def multiply_numbers(num):
    ans = 1
    for i in num:
        ans = ans * i

    return ans


# Todo6: Div
def div_numbers(num):
    ans = num[0] / num[1]

    return ans


# Todo7: Average

def avg_numbers(num):
    ans = 0
    for i in num:
        ans = ans + i
    ans = ans / len(num)
    return ans


greet('Glad to see you')
user_interface()
