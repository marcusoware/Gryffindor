"""
Working with modules

the use of in-build modules and exernal modules

"""



import random

def main():
    
   output = game_play()
   print(output)


def get_user_input():

    try:
        dice1 = int(input("enter first number: \n"))
    except (ValueError, TypeError):
        return "invalid input"
    
    try:
        dice2 = int(input("enter second number: \n"))
    except (ValueError, TypeError):
        return "invalid input"
    
    return dice1, dice2


def dice_game():

    dice1, dice2 = get_user_input()
    magic = random.randint(dice1, dice2)

    return magic


def game_play():

    while True:
        message = input(
            "Roll the dice? []'no'/ 'yes']"
        ).strip().lower()
        match message:
            case "n" | "no":
                return "program exited"
                
            case "y" | "yes":
               magic = dice_game()
               print(f"\nGuess Number:{magic}")
               print()
            case _:
                print( "invalid user choice")
                continue





if __name__ == "__main__":
    main()




'''item = random.choice(["car","shoe", "phone"])
print(item)


import cowsay

print(cowsay.trex('hello'))

'''



