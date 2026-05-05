import cv2

# Load the video
video = cv2.VideoCapture('./file/activate.mp4')
success, frame = video.read()
count = 0

while success:
    # Save each frame as a JPG
    cv2.imwrite(f'./file/frame{count}.jpg', frame)
    success, frame = video.read()
    count += 1

video.release() # Release resources [9]



