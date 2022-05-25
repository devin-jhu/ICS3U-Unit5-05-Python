#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The postal


def postal_address_function(
    name, street_number, street_name, city, province, postal_code, apartment=None
):

    # output
    if apartment != None:
        postal_address = "\n{0} \n{1}-{2} {3} \n{4} {5} {6}".format(
            name, street_number, street_name, city, province, postal_code, apartment
        )

    else:
        postal_address = "\n{0} \n{1} {2} \n{3} {4} {5}".format(
            name, street_number, street_name, city, province, postal_code
        )

    return postal_address.upper()


def main():

    apartment = None
    print("the postal address formater")
    # input
    name = input("Enter full name: ")
    street_number = input("Enter street number: ")
    street_name = input("Enter street name (include street/drive/ way): ")
    city = input("Enter city: ")
    province = input("Enter province (abbreviated form): ")
    postal_code = input("Enter postal code: ")
    question = input("Do you live in an apartment(y/n): ")
    if question == "y":
        apartment = input("Enter apartment number: ")

    # process
    if apartment is not None:
        apartment_number_int = int(apartment)
        if apartment_number_int < 0:
            print("\nNot a Street Number")
        # call functions
        else:
            proper_format_postal_address = postal_address_function(
                name,
                apartment,
                street_number,
                street_name,
                city,
                province,
                postal_code,
            )
            print(proper_format_postal_address)
    else:
        proper_format_postal_address = postal_address_function(
            name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
        )
        print(proper_format_postal_address)

    print("\nDone.")


if __name__ == "__main__":
    main()
