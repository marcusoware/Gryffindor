from PIL import Image

# open an image
img = Image.open("facebook.jpg")   
img.show()

# resize an image
img = Image.open("facebook.jpg")
resized = img.resize((250,300))
resized.show()

# convert an image format
img = Image.open("facebook.jpg")
img.save("newimage.jpg")
