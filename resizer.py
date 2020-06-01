import os
import sys
import cv2

path = 'E:\\Mega\\Photoshop\\outputs\\sofron_photography\\public\\'

filesList = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            filesList.append(os.path.join(r, file))

# for f in filesList:
    # print(f)

print(len(filesList))

pathname = os.path.dirname(sys.argv[0])
newpath = os.path.abspath(pathname) + r'\\resized\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print("Folder Created")
else:
    print("Folder already exists!")


print('path =', pathname)
print('full path =', os.path.abspath(pathname))

filenamesImages = []

for i in filesList:
    filenamesImages.append(i.split('\\')[-1])
width = 800
height = 800
#print(filenamesImages)
c = 0
print(filenamesImages[c])
for x in filesList:
    img = cv2.imread(x, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    print('Resized Dimensions : ',resized.shape)

    #cv2.imshow("Resized image", resized)
    location = os.path.abspath(pathname) + r'\\resized\\' + filenamesImages[c]
    print(location)
    cv2.imwrite(location,resized)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    c = c + 1
