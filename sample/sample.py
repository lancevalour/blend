import numpy as np
import cv2
import subprocess
import time

video = "C:/Users/ZhangY/Desktop/blend/temp.mp4"
output = "C:/Users/ZhangY/Desktop/blend/output.mp4"
image = "C:/Users/ZhangY/Desktop/pic/identicon.jpg"
scale_image = "C:/Users/ZhangY/Desktop/blend/image.jpg"
print(cv2.__version__)

# cap = cv2.captureFromFile(video)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
# start = time.time()
# subprocess.call("ffmpeg -i " + image + " -vf scale=10:-1 " + scale_image, shell=True)
# end = time.time()
# print(end - start)
#
start = time.time()

command = "ffmpeg -i " + video
overlay = " -filter_complex \""
images = ""
for i in range(0, 30):
    images += " -i " + scale_image
    if i == 0:
        overlay += "[0:v][1:v]overlay=10:10:enable='between(t,1,2)'[tmp]; "
    else:
        overlay += "[tmp][" + str(i + 1) + ":v] overlay=10:10:enable='between(t," + str(i + 1) + "," + str(
            i + 1.378) + ")'[tmp]; "

overlay = overlay[0: len(overlay) - 8] + "\" "
print(images)
command += images + overlay + output

print(command)

subprocess.call(command, shell=True)


# command += image + overlay

# command1 = "ffmpeg -i " + video + " -i " + scale_image + " -i " + scale_image + " -i " + scale_image + " -filter_complex " + \
#            "\"[0:v][1:v]overlay=10:10:enable='between(t,1,2)'[tmp]; " \
#            "[tmp][2:v] overlay=10:10:enable='between(t,3,4)'[tmp]; " \
#            "[tmp][3:v] overlay=10:10:enable='between(t,5,8)\" " + output
# print(command1)
#
# subprocess.call(command1, shell=True)
#
# end = time.time()
# print(end - start)
