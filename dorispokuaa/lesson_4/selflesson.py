data = ["book","pet",1.2,"pen","dog"]
'''
 for sentence in data:
     if sentence == "pen":
         continue
     else:
         print(sentence,"yes its working")

         
 print(data[0])
 data[0] = "doris"
print(data)

print(data[0])
data[0]="great"
print(data)

print(data[1])
data[1]="man"
print(data)

print(data[2])
data[2]="say" 
print(data)

print(data[3])
data[3]="get"
print(data)

print(data[4])
data[4]="van"
print(data)
print(data[1:])
while True:
    try:
        num = int(input("enter number: "))
        break
    except (TypeError, NameError, ValueError):
        print("please enter numbers only")
        continue

if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
    try:
    num = int(input("enter number" ))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
'''


try:
    num = int (input("enter number: "))
except ValueError:
    print("you have entered wrong input ") 


