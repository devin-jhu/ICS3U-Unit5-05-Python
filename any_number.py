#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The counter


def main():
    # this program counts
    counter = 1000

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("\n{0} ".format(counter), end=" ")
        else:
            print("{0} ".format(counter), end=" ")

    counter = counter + 1
    print("\nDone.")


if __name__ == "__main__":
    main()
