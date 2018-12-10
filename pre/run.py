# coding:utf-8
import glob
import os

from PIL import Image


def process(mov, atk, savename):
    """
    @param mov: move file 
    @param atk: atk file 
    @param savename: savefile
    """
    image = Image.new('RGBA', (256,448), (0,0,0,0))
    mov_img = Image.open(mov)
    atk_img = Image.open(atk)

    for x in range(0,4):
        crop_box = (0, x*64,64,(x+1)*64)
        crop = atk_img.crop(crop_box)
        paste_box = (x*64,0,(x+1)*64,64)
        image.paste(crop, paste_box)

    row = 1
    for x in range(0,4):
        crop_box = (0, (x+4)*64,64,(x+1+4)*64)
        crop = atk_img.crop(crop_box)
        paste_box = (x*64,row*64,(x+1)*64,(row+1)*64)
        image.paste(crop, paste_box)

    row = 2
    for x in range(0,4):
        crop_box = (0, (x+8)*64,64,(x+1+8)*64)
        crop = atk_img.crop(crop_box)
        paste_box = (x*64,row*64,(x+1)*64,(row+1)*64)
        image.paste(crop, paste_box)

    row = 3
    for x in range(0,4):
        crop_box = (0, (x+8)*64,64,(x+1+8)*64)
        crop = atk_img.crop(crop_box).transpose(Image.FLIP_LEFT_RIGHT)
        paste_box = (x*64,row*64,(x+1)*64,(row+1)*64)
        image.paste(crop, paste_box)

    row = 4
    for x in range(0,2):
        crop_box = (0, x*48,48,(x+1)*48)
        crop = mov_img.crop(crop_box)
        paste_box = (x*64+8,row*64+8,(x+1)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)
    for x in range(0,2):
        crop_box = (0, (x+2)*48,48,(x+1+2)*48)
        crop = mov_img.crop(crop_box)
        paste_box = ((x+2)*64+8,row*64+8,(x+1+2)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)

    row = 5
    for x in range(0,2):
        crop_box = (0, (x+4)*48,48,(x+1+4)*48)
        crop = mov_img.crop(crop_box)
        paste_box = (x*64+8,row*64+8,(x+1)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)
    for x in range(0,2):
        crop_box = (0, (x+4)*48,48,(x+1+4)*48)
        crop = mov_img.crop(crop_box).transpose(Image.FLIP_LEFT_RIGHT)
        paste_box = ((x+2)*64+8,row*64+8,(x+1+2)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)

    row = 6
    for x in range(0,2):
        crop_box = (0, (x+6)*48,48,(x+1+6)*48)
        crop = mov_img.crop(crop_box)
        paste_box = (x*64+8,row*64+8,(x+1)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)
    for x in range(0,2):
        crop_box = (0, 8*48,48,9*48)
        crop = mov_img.crop(crop_box)
        if x == 1:
            crop = crop.transpose(Image.FLIP_LEFT_RIGHT)
        
        paste_box = ((x+2)*64+8,row*64+8,(x+1+2)*64-8,(row+1)*64-8)
        image.paste(crop, paste_box)

    image.save(savename)

def main():
    srcdir = r"E:\work\github\gamesanguo\sanguo\resource\solders"
    for x in range(0,5):
        for y in range(0,5):
            for z in range(0,5):
                atk_filename = "atk_{}_{}_{}.png".format(x,y,z)
                mov_filename = "mov_{}_{}_{}.png".format(x,y,z)
                atk_path = os.path.join(srcdir, atk_filename)
                mov_path = os.path.join(srcdir, mov_filename)
                if os.path.exists(atk_path):
                    savepath = "{}_{}_{}.png".format(x,y,z)
                    process(mov_path,atk_path,savepath)

if __name__ == '__main__':
    main()