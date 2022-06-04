 #!/usr/bin/env python3

# Created by: Sarah
# Created on: June 4th, 2022.
# This program allows the user to select a task they'd like to complete. It
# removes duplicates in a list, as well as, determing the length of an element
# in a list.

# this function determines the length of each element in the list
def size_of_str(size):
    # delcare empty size
    list_size = []
    for counter in range(len(size)):
        list_size.append(len(size[counter]))
    return list_size

# this function removes any duplicates in a list 
def duplicate(list_1):
    temp_list = []

    for element in list_1:
        if element not in temp_list:
            temp_list.append(element)
    removed_dup = temp_list
    return removed_dup
    # code above from guru99.com
  

def main():
    # declare an empty list
    size_of_list = []
    element_size = []
    list_string = []
    
    print("Today, you'll get to select what you'd like to complete.")
    print("Option 1: Determing the length of the elements in a list.")
    print("Option 2: Removing duplicates in a list.")
    print("Please select either or to continue.")
    print("")
    
    while True:
        selector = input("Choose which game you'd like to execute (1, 2): ")
        
        if selector == "1":
            # gets user input
            list_str = input("Enter a list of strings (ex hi, wecome): ")
            size_of_list = list_str.split(", ")
            
            # adding string to the end of the list
            for string in size_of_list:
                element_size.append(string)
            
            # calls function
            final_list = size_of_str(element_size)
            
            # prints final formated list
            print("")
            print("The length of each string is: {}".format(final_list))
            break
        
        elif selector == "2":
            # get user input
            user_str = ("Enter a list of elements: ")
            list_string = user_str.split(", ")
                
            for elements in list_string:
                a_num = elements
                list_string.append(a_num)
                print("")
                
            dup_list = duplicate(a_num)
            print("The list after removing duplicates is: {}".format(dup_list))
            break
        else:
            print("Invalid, please select either or.")
            print("")
        
if __name__ == "__main__":
    main()
