
# creating a parity function to determine if a number is even or odd:

# # creating a parity to take in users input:
# def parity():
#     num = int(input("choose and number : "))
# # use % 2 to check for even numbers: 
#     if num % 2 == 0:
#         print(f" Your number '{num}' is even")
# #  using % 3 to check for odd numbers:
#     elif num % 3 == 0:
#         print(f"Your number '{num}' is odd")
#     else:
#         print(f"Your number '{num}' is prime") 

# parity()   



# using try and except function to pass an error.
def parity():
    while True:
        try:
            num = int(input("choose and number  "))
        except ValueError:
            print("is not an integer")
            break
            if num % 2 == 0:
                print(f" Your number '{num}' is even")
            elif num % 3 == 0:
                print(f"Your number '{num}' is odd")
            else:
                print(f"Your number '{num}' is prime") 
parity()   






