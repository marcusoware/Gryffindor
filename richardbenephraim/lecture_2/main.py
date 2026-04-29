"""

loops


"""



# while loop

i = 3

# while i != 0:
#     print(i)
#     i-=1




#for loop
animal = "cat"

# for _ in animal:
#     print(_)

# for letter in range(len(animal)):
#     print(letter)
#     print(animal[letter])


# for index, letter in enumerate(animal):
#     print(index, letter)


def main():
    #build_length()
    #build_width()
    length = cal("###", "##")
    print(length)


def build_width():
    num = int(input("enter number: "))

    for _ in range(num):
        print("#"*num)


def build_length():
    for _ in range (10):
        print("#", )


def cal(width, height):
    return width + "\n" + height


def get_input():
    num = int(input("enter number: "))
    return num


def box_maker():
    for _ in range(get_input):
        return f"#"*get_input
    










if __name__ == "__main__":
    #main()
    pass
    

# Error Handling

try:
    print(a)
except NameError:
    print("variable is not assigned... please")


# print(a+3)
