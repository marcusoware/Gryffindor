'''
          ===== Currency Converter=====

    Write a program to convert an amount of money from one currency to another

    using fixed exchange rates. The user inputs the amount and selects the currencies

    for conversion.

TODO =>

    Optional Enhancements

    • Expand the list of available currencies for conversion. This might involve
    adding more fixed exchange rates to the program.

'''


def main():
    output =choice()
    print(output)



def get_user_input():
    while True:
        try:
            amount = float(input("Enter amount: \n"))
            break
        except (ValueError, TypeError) as e:
            print("invalid input  ",e)
            continue
    Source = input ("Source of Currency: \n \n1: GHC \n2: USD \n3: EUR \n4: GBP \n ").strip().upper()

    Target = input ("Target  Currency: \n \n1: GHC \n2: USD \n3: EUR \n4: GBP \n ").strip().upper()
  
    


#return the variable to the function so u can use it in another function

    return amount, Source, Target

"""
define a function to control the flow of the conversion
use match-case for the initial flow then
use if -else for checking the source And target choice
"""

def choice():

    header = f"*"*10, "CURRENCY CONVERTER", f"*"*10 

    message = input (
        f"\n{header}\n"
        f"\npress 1 continue \n"
        f"press 'n' to exit\n"
        "Enter your desire choice: \n"
    ).strip().lower()

    print()

    match message:
        case "n":
            return "program exited ..."
        case _:
            amount, source, Target = get_user_input()
            if source == "1":

                if Target == "1":
                    return f"GHC{amount}"
                
                elif Target == "2":
                    return ghc_to_usd(amount)
                
                elif Target == "3":
                    return ghc_to_euro(amount)
                
                elif Target == "4":
                    return ghc_to_gbp(amount)
                
                else:
                    return "invalid Target Currency choice"
                
            elif source == "2":
                if Target == "1":
                    return usd_to_ghc(amount)
                elif Target == "2":
                    return f"USD{amount}"
                elif Target == "3":
                    return usd_to_euro(amount)
                elif Target == "4":
                    return usd_to_gbp(amount)
                else:
                    return "invalid Target Currency choice"
            elif source == "3":
                if Target == "1":
                    return euro_to_ghc(amount)
                elif Target == "2":
                    return euro_to_usd(amount)
                elif Target == "3":
                    return f"EUR{amount}"
                elif Target == "4":
                    return euro_to_gbp(amount)
                else:
                    return "invalid Target Currency choice"
            elif source == "4":
                if Target == "1":
                    return gbp_to_ghc(amount)
                elif Target == "2":
                    return gbp_to_usd(amount)
                elif Target == "3":
                    return gbp_to_euro(amount)
                elif Target == "4":
                    return f"GBP{amount}"
                else:
                    return "invalid Target Currency choice"
            else:
                return "invalid input... Try Again"

            
# a function each to do the conversion 
def usd_to_ghc(amount: float):


    cash = amount * 11.25
    return f'GHC {cash:.2f}'

def ghc_to_usd(amount: float):
    cash = amount * 0.091
    return f"USD {cash:.2f}"


def euro_to_ghc(amount:float):
    cash = amount * 12.93
    return f"GHC {cash:.2f}"

def ghc_to_euro(amount: float):
    cash = amount * 0.08
    return f"EUR {cash:.2f}"


def gbp_to_ghc(amount: float):
    cash = amount * 14.81
    return f"GHC{cash:.2f}"

def ghc_to_gbp(amount: float):
    cash = amount * 0.07
    return f"GBP {cash:.2f}"


def usd_to_euro(amount: float):
    cash = amount * 0.85
    return f"EUR {cash:.2f}"

def euro_to_usd(amount:float):
    cash = amount * 1.18
    return f"USD {cash:2f}"

def usd_to_gbp(amount: float):
    cash = amount * 0.74
    return f"GBP {cash:.2f}"

def gbp_to_usd(amount: float):
    cash = amount * 1.35
    return f"USD {cash:.2f}"

def euro_to_gbp(amount: float):
    cash = amount * 0.87
    return f"GBP {cash:.2f}"

def gbp_to_euro(amount: float):
    cash = amount * 1.14
    return f"EUR {cash:.2f}"


if __name__ == "__main__":
    main()