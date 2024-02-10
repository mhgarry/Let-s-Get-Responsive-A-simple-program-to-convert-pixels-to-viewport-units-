# ask user if they want to convert pixels to vw or vh units 
# ask user for the number of pixels
# ask user for the viewport width or height
# calculate the vw or vh units
# print the result
# ask user if they want to convert more pixels
# if yes, repeat the process
# if no, end the program 
def main():
  print("Welcome to the viewport width and height calculator.")
  while True:
    print("Would you like to convert pixels to vw or vh units?")
    print("Enter 'vw' for viewport width or 'vh' for viewport height.")
    user_input = input("Enter your choice: ")
    if user_input == "vw":
      # if user enters vw, define and call the px_to_vw function
      def px_to_vw():
        px = int(input("Enter the number of pixels: "))
        vw = int(input("Enter the viewport width: "))
        result = px / vw * 100
        print(f"{px} pixels is equal to {result}vw.")
      # call the px_to_vw function
      px_to_vw()