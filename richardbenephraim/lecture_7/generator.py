from os import path


def id_generation():
         
    start = 1

    while start > 0:
        yield start

        start +=1
      
dd = id_generation()
print(next(dd))
print(next(dd))
print(next(dd))
print(next(dd))
