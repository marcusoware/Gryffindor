# # create a function
# def main():
#     parity()


# def parity():
#Taking a user input
#     num = int(input("Enter a number : "))

# Using a while loop
#     while True:
#         if num % 2 == 0:
#             print("is even")
#         else:
#             print("is odd")
#         break


# Calling the function
# main()


# create a functin
def main():
    parity()


def parity():
    # Taking a user input
    try:
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            print("is even")
        else:
            print("is odd")
    except ValueError:
        print("not an integer")

            

main() 