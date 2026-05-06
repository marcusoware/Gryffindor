


def main():
    file_handling()
    

def file_handling():
    
    with open("../lecture_5/texts.txt", "w") as file:
        file.write("hello this is another file working in lecture 6 ")

    file = open("text.txt","w",encoding="utf-8")
    file.write("this is working")
    file.close()





   


if __name__ == "__main__":
    main()