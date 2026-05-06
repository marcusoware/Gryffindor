


def decorator(f):
    def wrapper():
        print("start")
        f()
        print("end")
        return f()
    return wrapper



@decorator
def square():
   
    total = 2**2
    return total

a = square()
print(a)
