def mydecorator(f):
    def wrapper():
        print("start")
        f()
        print("end")
    return wrapper

def square(): 
    return 20**3
t = square()
print(t)
