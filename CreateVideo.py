import os
import cv2

path = "Imagens/"

Imagens = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        file_name = os.path.join(path, file)
        Imagens.append(file_name)
        print(file_name)

count = len(Imagens)

frame = cv2.imread(Imagens[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    image = cv2.imread(Imagens[i])
    out.write(image)

out.release()
print("Concluído")



