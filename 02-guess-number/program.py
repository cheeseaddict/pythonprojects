import random


def print_header():
    print("--------------------------------")
    print("		  Guess The number")
    print("--------------------------------")


def guess_number():
    number = random.randint(0, 100)

    while True:
        guess = int(input("Guess a number between 0 and 100: "))
        if guess < number:
            print("Sorry but {} was LOWER than the number".format(guess))
        elif guess > number:
            print("Sorry but {} was HIGHER than the number".format(guess))
        else:
            print("YES! You've got it. The number was {}".format(number))
            break


def main():
    print_header()
    guess_number()


main()