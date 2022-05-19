import os
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def getPathFolder():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    return folder

def resizer(p):
    lists = os.listdir(p)
    print(lists)
    for i in lists:
        # print(i)
        new_folder = p + "/" + "output"
        # os.makedirs(new_folder) 
        if ".jpg" in i:
            filename, file_extension = os.path.splitext(i)
            basewidth = 300
            image_loc = p + "/" + i
            # print(image_loc)
            img = Image.open(image_loc)
            width, height = img.size
            # print(width)
            # print(height)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img = img.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
            new_name = p + filename + "_resized" + file_extension
            # print(new_name)
            img.save(new_name)

def main():
    path_folder_destination = getPathFolder()
    resizer(path_folder_destination)


if __name__ == '__main__':
    main()
