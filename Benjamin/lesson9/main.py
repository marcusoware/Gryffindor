class Calculator:
    def __init__(self):
        self.memory = 0
        
        

    def addition(self, num1, num2):
        self. total = num1 + num2
        return self.total
    
    def subtraction(self, num1, num2):
        self.total = num1 - num2
        return self.total
    
    def multiplication(self, num1, num2):
        self.total = num1 * num2
        return self.total


        
    def get_userinput(self, ):
        self.num1 = int(
            input("enter first number: ")
        )
        self.num2 = int(
            input("enter first number: ")
        )

        self.message = input(
            "select the operation\n"
            "[+] [-] [*]\n"
        )
    
        if self.message == "+":
            return self.addition(self.num1, self.num2)
        elif self.message == "-":
            return self.subtraction(self.num1, self.num2)
        elif self.message == "*":
            return self.multiplication(self.num1, self.num2)
        else:
            return "invalid user choice"



my_calcus = Calculator()

print(my_calcus.get_userinput())
