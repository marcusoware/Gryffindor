from time import sleep

def Traffic_light():
    for i in range(3):
        print("***********")
        print("Red")
        print("***********")
        sleep(5)
        print("Yellow")
        print("***********")
        sleep(1)
        print("Green")
        print("Go")
        print("***********")
        
if __name__== "_main_":
    traffic_light()