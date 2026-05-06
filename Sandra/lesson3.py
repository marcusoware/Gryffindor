#import random
#from random import randint
#from random import randint as rd
#from random import randint,choices
#print(randint(10,15))
#print(choices([app]))

#from sys import argv
#print(argv)

#print(sys.argv)
#-m venv .venv

#import sys
#if sys.argv[1:]:
#    if sys.argv[1] == "-m":
#        print("module")
#    elif sys.argv[2] == "-p":
#         print("path") 
#    else:
#        print("too few arguments")

#import cowsay

#print(cowsay.trex("hello"))

#fd = open("./mock(1).csv")

#content = fd.readlines()
#print(content[10:50])

#for line in fd.readlines():
#    print(line)
   
#fd.close()   
#import PIL
#importing a picture from PIL import image, image chops


from PIL import Image, ImageChops

img1 = Image.open('./Me1.jpeg')
img2 = Image.open('./Me2.jpeg')

diff = ImageChops.difference(img1,img2)
diff.show()
