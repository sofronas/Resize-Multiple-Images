#=========================================#
# Resizer Image Program                   #
# Email: sofronas.konstantinos@gmail.com  #
# Name: Sofronas Konstantinos Sotirios    #
# Website: https://sofronas.github.io     #
#=========================================#

import os
import sys
import cv2
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

typeOfImageUser = "empty"


def UserSelectTypeOfImage():
    window = Tk()
    window.geometry('100x100')
    def close():
        # print(variable.get())
        x = variable.get()
        # print(typeOfImageUser)
        window.destroy()
        global typeOfImageUser
        typeOfImageUser = x

    variable = StringVar(window)
    variable.set("png") # default value
    w = OptionMenu(window, variable, "png", "jpg")
    w.pack()
    closebutton = Button(window, text='X', command=close)
    closebutton.pack()
    window.mainloop()


def setPhotoParametersW():
    getWH = Tk()

    canvas1 = Canvas(getWH, width = 400, height = 300)
    canvas1.pack()

    entry1 = Entry (getWH)
    canvas1.create_window(200, 140, window=entry1)

    def getW ():
        x1 = entry1.get()
        getWH.destroy()
        print(x1)
        global width
        width = int(x1)

    button1 = Button(text='Get the Width', command=getW)
    canvas1.create_window(200, 180, window=button1)
    getWH.mainloop()

def setPhotoParametersH():
    getWH = Tk()

    canvas1 = Canvas(getWH, width = 400, height = 300)
    canvas1.pack()

    entry1 = Entry (getWH)
    canvas1.create_window(200, 140, window=entry1)

    def getH ():
        x1 = entry1.get()
        getWH.destroy()
        print(x1)
        global height
        height = int(x1)

    button1 = Button(text='Get the Height', command=getH)
    canvas1.create_window(200, 180, window=button1)
    getWH.mainloop()


root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
root.destroy()

path = folder_selected.replace("/","\\")
# print("Path of Images Secelected: {}" .format(path))

typeOfImage = '.jpg' # By default is jpg
UserSelectTypeOfImage()
typeOfImage = typeOfImageUser
print("User gave: {}" .format(typeOfImageUser))

filesList = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if typeOfImageUser in file:
            filesList.append(os.path.join(r, file))

if len(filesList) == 0:
    print("No photos\n")
    exit()
else:
    print("Photos Included: {}" .format(len(filesList)))


pathname = os.path.dirname(sys.argv[0])
newpath = path + r'\\resized\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print("Folder Created")
else:
    print("Folder already exists!")

# print('full path =', os.path.abspath(pathname))

filenamesImages = []

for i in filesList:
    filenamesImages.append(i.split('\\')[-1])


width =  100 # Default Value
height = 100 # Default Value

setPhotoParametersW()
setPhotoParametersH()


c = 0
for x in filesList:
    img = cv2.imread(x, cv2.IMREAD_UNCHANGED)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    location = path + r'\\resized\\' + filenamesImages[c]
    cv2.imwrite(location,resized)
    cv2.destroyAllWindows()
    c = c + 1
print("Process Finished")


finishBox = Tk()
finishBox.withdraw()
messagebox.showinfo("Process", "Job Finished")
