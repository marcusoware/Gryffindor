# with open("files/MOCK_DATA.csv", "r", encoding="utf-8") as file:
#    content = file.readlines()

# for txt in content[:51]:
#    pass
   


from PIL import Image, ImageChops
from os import path 

base_dir = path.join("files", "a.JPG")
base_dir2 = path.join("files", "b.JPG")


img1 = Image.open(base_dir)
climg2 = Image.open(base_dir2)

difference = ImageChops.difference(img1,climg2)

difference.show()

