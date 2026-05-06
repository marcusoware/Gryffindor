

def main():
    parity = parity_function("enter number: \n")
    print(parity)



def parity_function(prompt):
    
    while True:
        try:
            number = int(input(prompt))
            break
        except (TypeError, ValueError) as e:
            print(e, " __ Please number ")
            continue

    if number % 2 == 0:
        return "number is Even"
    
    else:
        return "Number is Odd"
    


if __name__ == "__main__":
    main()