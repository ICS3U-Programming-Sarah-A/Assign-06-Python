#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 4th, 2022.
# This program allows the user to select a task they'd like to complete. It
# removes duplicates in a list, as well as, determining the length of an 
# element in a list.


# this function determines the length of each element in the list
def size_of_str(size):
    # declare empty list
    list_size = []
    for counter in range(len(size)):
        list_size.append(len(size[counter]))
    return list_size


# this function removes any duplicates in a list
def duplicate(list_1):
    temp_list = []
    print("This is the list before removed duplicates: {}".format(list_1))

    for element in list_1:
        if element not in temp_list:
            temp_list.append(element)

    # sorts the list then returns it to main
    temp_list = sorted(temp_list)
    return temp_list
    # code modified from guru99.com


def main():
    # declare an empty lists
    size_of_list = []
    element_size = []
    list_string = []
    final_dup_list = []

    print("Today, you'll get to select what you'd like to complete.")
    print("Option 1: Determining the length of the elements in a list.")
    print("Option 2: Removing duplicates in a list.")
    print("Please select either or to continue.")
    print("")

    while True:
        # gets user input
        selector = input("Choose which game you'd like to execute (1, 2): ")

        if selector == "1":
            # gets user input
            list_str = input("Enter a list of strings (ex hi, welcome): ")
            size_of_list = list_str.split(", ")

            # adding string to the end of the list
            for string in size_of_list:
                element_size.append(string)

            # calls function
            final_list = size_of_str(element_size)

            # prints final formatted list
            print("")
            print("The length of each string is: {}".format(final_list))
            break

        # if user selects option 2, do the following...
        elif selector == "2":
            # get user input
            user_str = input("Enter a list of elements: ")
            list_string = user_str.split(", ")

            for num_str in list_string:
                a_element = num_str
                final_dup_list.append(a_element)

            print("")
            # calls function & displays removed duplicates
            duplicated_list = duplicate(final_dup_list)
            print("The list after removing duplicates is: {}"
                  .format(duplicated_list))
            break
        else:
            print("Invalid, please select either or being 1 or 2.")
            print("")


if __name__ == "__main__":
    main()
