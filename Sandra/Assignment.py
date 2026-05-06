#creating a parity function to determine if a number is even or odd

def parity(num):
    if num% 2 == 0:
        return "even"
    else:
        return "odd"
    
num = int(input("Enter a number: "))
print(parity(num))    


#Using try and except function to pass an error.

def parity(num):

    if num% 2 == 0:
        return "even"
    else:
        return "odd"
    
while True:    
    try:
        user_input = int(input("Enter num: "))
        print(parity(user_input))
        break
    
    except(ValueError,TypeError):
        print("Invalid input") 
     