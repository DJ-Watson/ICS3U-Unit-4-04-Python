#!/usr/bin/env python3

# Created by DJ Watson
# Created on October
# this program is a guessing game where the user has to guess a number
# that the system has in memory


import random

random = random.randint(1, 9+1)


def main():
    # input

    numinput = input("Guess the number I am thinking of (1-10): ")
    print("")
    # process and output

    for loop_n in range(5):
        try:
            intcheck = int(numinput)
            if intcheck == random:
                print("Correct!")
                break
            else:
                print("Incorrect!")
                if loop_n == 4:
                    break
                else:
                    numinput = input("Try again: ")
                    print("")
        except ValueError:
            print("Invalid input")
            numinput = input("try again: ")
    print("The number was: {}".format(random))
    print("")
    print("Attempts: {}".format(loop_n+1))


if __name__ == "__main__":
    main()
