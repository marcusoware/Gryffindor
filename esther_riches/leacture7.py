'''content=id.readlines()
for line in id.readlines()[:50]:
    id.closed()
    for line in content:
        print(line)
'''


from PIL import Image, ImageChops
# open an image file
img1=Image.open("image.jpeg")

img2=Image.open("image2.jpeg")


difference = ImageChops.difference(img1,img2)
difference.show()




