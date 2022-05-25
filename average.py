#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The counter


import random


def main():
    # this function finds the average of 10 random numbers

    number_array = []

    print("The random number average finder")

    # process
    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_array.append(random_number)
        print("Random number: {}".format(random_number))

    average = sum(number_array) / 10

    # output
    print("\nThe average is {0:.1f}.".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
