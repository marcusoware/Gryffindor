
import sys
import argparse

arr = [1, 2, 3, 5, 5, 7 , 8]

print(set(arr))

a  = arr


print(a)


def generator():

    start = 1
    while start >= 0:

        yield start

        start +=1



aa = generator()

print(next(aa))
print(next(aa))



def gg():

    for i in range(1, 10):
        yield i


aa = gg()
print(next(aa))
print(next(aa))


arr = [a for a in range(10) if a %2 == 0]
print(arr)
