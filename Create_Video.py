import cv2
import os

path = "Images/"

Imagesss = []

for i in os.listdir(path):
    name , extension = os.path.splitext(i)
    if extension in [".gif",".jpg",".jpeg","png",".jfif"]:
        path1 = path+"/"+i
    Imagesss.append(path1)

count = len(Imagesss)

frame = cv2.imread(Imagesss[0])
width , height , channel = frame.shape

size = (height,width)

out = cv2.VideoWriter("Project.avi" , cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for j in range(0, count-1):
    frame = cv2.imread(Imagesss[j])
    out.write(frame)
out.release()

print("Done!")