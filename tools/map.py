# coding:utf-8
import  numpy as np
import cv2
import glob

mapname = r"D:\workspace\github\gamesanguo\images\map\anding.jpg"


sources = glob.glob(r'D:\workspace\github\gamesanguo\images\tiles\*.bmp')
imgs = []
for source in sources:
    im = cv2.imread(source,0)
    imgs.append(im)

img = cv2.imread(mapname, 0)

rows, cols = img.shape

for r in range(0, rows, 17):
    for c in range(0, cols, 17):
        roi = img[r:r+16,c:c+16]
        for im in imgs:
            sub = roi - im
            s = np.sum(sub)
            print(s)
