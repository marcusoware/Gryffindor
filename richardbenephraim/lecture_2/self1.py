"""
Build Terminal Quiz Game


"""

from self1_quiz import python_questions



def main():
    out = front_page()
    print(out)



def quiz_game():
    print("Quiz Loggeding \n  ")
    choice = {
            "a" : 0,
            "b" : 1,
            "c" : 2,
            "d" : 3
        }
    
    counter = 1

    for question in python_questions:
        while True:
            message = input (
                f"\n  \n{counter}: {question[0]} \n{"*"*5} OPTIONS {"*"*5}\nA: {question[1][0]} \nB: {question[1][1]} \nC: {question[1][2]} \nD: {question[1][3]}\n").strip().lower() 
            if message not in ["a","b","c","d"]:
                print("invalid user choice ")
                continue
            else:
                break
        if choice.get(message) == question[2]:
            print("correct! ")
            print(f"you have won GH{counter*100}cedis")
            
            """
             with open("answer.txt", "a", encoding="utf-8")as file:   
                file.write(message + "\n") => will later on it
            """
            
                    
        else:
            print ("wrong! ")
        counter +=1
        print()

def front_page():
    for v in range (10):
        print("#", end=" ")
        
    for b in range(5):
        print("#", )

        if b == 2:
            print("#","  PYTHON QUIZ GAME  ")
    for c in range(11):
        print("#", end=" ")
    
    print()
    message = input(" \nPress '1' to start the game of '2'to exist game: \n")
    match message:
        case "1":
            quiz_game()
            
        case "2": 
            return "Program Logged out ..."
        case _:
            return "invalid user input1"

if __name__ == "__main__":
    main()

