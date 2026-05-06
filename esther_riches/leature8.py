



from PIL import Image, ImageEnhance
# Open image.
image=Image.open("image.jpeg")

frames=[]
# create brightness animation
for i in range(5):
    enhancer=ImageEnhance.Brightness(image)
    frame=enhancer.enhance(0.5+i*0.3) # change brightness
    frames.append(frame)


    # save as GIF
    frames[0].save("output.gif",
                   save_all=True,
                   append_images=frames[1:],
                   duration=300,
                   loop=0
                   )
    print("GIF created successfully!")
                 