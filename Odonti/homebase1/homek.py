import random

coin = random.choice(["Heads", "Tails", "legs"])
print(coin)


import math
print(math.sqrt(16))
print(math.sqrt(12,))
print(math.sqrt(25))


import random

number = random.randint(1, 10)
print(number)

import random

cards = ["queen", "king", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)


# import random
# names = ["ben", "gifty", "son", "joy"]
# random.shuffle((names))
# for name in names:
#     print(name)


import random
names = random.choice(["ben", "gifty", "son", "joy"])
print(names)

# using a statistics library:
import statistics
print(statistics.mean([100, 90]))

# # using the sys and argv:
# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few argument")



import sys

if len(sys.argv) <2:
    print("Too few argument")
elif len(sys.argv) >2:
    print("Too many argument")
else:
    print("Hello my name is", sys.argv[1])


import sys
if len(sys.argv) < 4:
    print("I love")
elif len(sys.argv) > 4:
    print("You are my enemy")
else:
    print("Come home", sys.argv[6])