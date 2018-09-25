# coding:utf-8
import  numpy as np
import cv2
import glob
import os

from PIL import Image

r = 247
g = 0
b = 255
def trans(srcfile, dstfile):
    img = Image.open(srcfile)
    im2 = img.convert('RGBA')

    size = im2.size
    #print(size)
    for x in range(size[0]):
        for y in range(size[1]):
            color = im2.getpixel((x,y))
            #print(color)
            if color[0] == r and color[1]==g and color[2]==b:
                im2.putpixel((x,y),(color[0],color[1],color[2],0))

    im2.save(dstfile)

savedir = r"D:\workspace\github\gamesanguo\sanguo\resource\solders"
files = glob.glob(r"E:\游戏用照片\三国\图片\caocao传\*.bmp")
for file in files:
    basename = os.path.basename(file)
    dstname = basename[0:-6] +".png"
    dstfile = os.path.join(savedir, dstname)
    print(dstfile)
    trans(file, dstfile)
