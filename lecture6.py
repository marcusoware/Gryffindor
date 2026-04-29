# file = open("text.txt","w")
# file.write("append")
# file.close()
 
fd = open('./mock.csv')

content = fd.readlines
print(content[:50])
for line in fd.readlines():
    print (line)

fd.close() 


from PIL import Image,ImageChops


img1 = Image.open('./         ')
img2 = Image.open('./         ')

diff = ImageChops.difference(img1,img1)
diff.show()



