from PIL import Image, ImageChops
import os

file_path = os.path.join("image1.jpeg")
file_path2 = os.path.join( "image2.jpeg")



img1 = Image.open(fp=file_path) #first image path in str

img2 = Image.open(fp=file_path2)


diff = ImageChops.difference(img1, img2)
diff.show()