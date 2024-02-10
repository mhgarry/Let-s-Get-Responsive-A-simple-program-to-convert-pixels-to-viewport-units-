# # ask user if they want to convert pixels to vw or vh units 
# # ask user for the number of pixels
# # ask user for the viewport width or height
# # calculate the vw or vh units
# # print the result
# # ask user if they want to convert more pixels
# # if yes, repeat the process
# # if no, end the program 
def main():
    print("Welcome to the viewport width and height calculator.")
    while True:
        print("Would you like to convert pixels to vw or vh units?")
        print("Enter 'vw' for viewport width or 'vh' for viewport height.")
        user_input = input("Enter your choice: ")
        # if user enters vw, define and call the px_to_vw function
        if user_input == "vw":
            result, units = px_to_vw()
        # skip to this line if user enters vh
        elif user_input == "vh":
            result, units = px_to_vh()
        # call the save_results function to ask user if they want to write the results to a txt file
        save_results(result, units) 
        
        print("Would You Like to convert more pixels?")
        print("Enter 'yes' to convert more pixels or 'no' to end the program.")
        # ask the user if they want to convert more pixels or end the program
        user_input = input("Enter your choice: ")
        if user_input == "no":
            print("Thank you for using the viewport width and height calculator.")
            break
        elif user_input == "yes":
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
# define the px_to_vw function 
def px_to_vw():
    units = "vw"
    px = int(input("Enter the number of pixels: "))
    vw = int(input("Enter the viewport width: "))
    result = px / vw * 100
    print(f"{px} pixels is equal to {result}{units}.")
    # return result and units to use in the save_results function
    return result, units
# define the px_to_vh function
def px_to_vh(units="vh"):
    px = int(input("Enter the number of pixels: "))
    vh = int(input("Enter the viewport height: "))
    result = px / vh * 100
    print(f"{px} pixels is equal to {result}{units}.")
    # return result and units to use in the save_results function
    return result, units  
# prompt user to save the results to a txt file
def save_results(result, units):
    print("Would you like to write the results to a txt file?")
    print("Enter 'yes' to write the results to a txt file or 'no' to skip.")
    user_input = input("Enter your choice: ")
    if user_input == "yes":
        write_to_file(result, units)
# if user enters yes, create a new file or append the results to an existing file in the current directory named "conversion_results.txt"
def write_to_file(result, units):
    filename = "conversion_results.txt"
    with open(filename, "a") as file:
        file.write(f"{result}{units}\n")

# call the main function to run the program
if __name__ == "__main__":
    main()
