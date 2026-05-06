
import time



def main():
    
    traffic_light()



def traffic_light():

   for var in range(6):
       print("==================")
       print("RED")
       time.sleep(5)
       print("===================")
       print("YELLOW")
       time.sleep(5)
       print("=======================")
       print("GREEN")

       
       time.sleep(5)
       print("==============================")
       print("GO")
       time.sleep(10)

if __name__ == "__main__":
    main() 