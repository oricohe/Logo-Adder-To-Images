from PIL import Image
import glob
from datetime import datetime
import os
import imageio
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd

# progres display (in the cmd)
def progress(percent=0,now = 0, all = 0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}% ', all,"/",now,
          sep='', end='', flush=True)


def logoim(filename, logo_file):
    originalIm = Image.open(filename) #Open the image
    width, height = originalIm.size #Taking sizes
    logoIm = Image.open(logo_file)
    width2, height2 = logoIm.size
    logoRatio = width2/height2 #Fixed aspect ratio of the logo
    # print("width = " + str(width) + " height = " + str(height))
    image = imageio.imread(filename)
    # print shape of the image
    h, w, a = image.shape


    width_new = int((height/21)*logoRatio)
    height_new = int(height/21)
    quarterSizeIm = logoIm.resize((width_new, height_new))
    newIm = originalIm.copy() #Make copy of original cat image
    newIm.paste(quarterSizeIm, (width-width_new,height-height_new)) #Paste the cropped portio# n
    if h > w:
            newIm = newIm.transpose(Image.ROTATE_90)
    return newIm

def quality( width, height,newIm):
    widthnew, heightnew = newIm.size
    if widthnew == width and heightnew == height:
        return 'True'
    return 'False'

def main():


#   path_old_folder = input("Enter the folder's path of the original images (with r):")
#   path_new_folder = input("Enter the folder's path of the new images (with r:")
#   file_type = input("Enter the file type of the original images: (jpg/png)")
#    file_type = 'jpg'

    file_type = 'jpg'
    new_file_type = 'jpg'
 #   new_file_type = input("Enter the file type of the new images: (jpg/png)")
    print("Please select the folder with the images.")
    folder = askdirectory()
#    folder = ("r'" + folder + "'")
    path_old_folder = folder
    a = True
    while a:
#        folder_name = input("Enter the name of the new folder(only letters and numbers):")
        print("Please select the location of the new directory.")
        folder2 = askdirectory()
#        folder2 = ("r'" + folder2 + "'")
        path_new_folder =  (folder2) + "\logo"
        print(path_new_folder)
        if not os.path.exists(path_new_folder):
            a = False
            os.makedirs(path_new_folder)

  #  logo_file = input("Enter the file path of the logo (with .png/.jpg):")
#    logo_file = 'LOGO+.jpg'
    print("Please select the image of the logo.")
    filename = fd.askopenfilename()
    logo_file = filename
    index = 0
    print("ok")

    i = 0
    print(path_old_folder)
    for filename in glob.glob(path_old_folder + '/*.' + file_type):
        print(filename)
        i += 1
    print(i)
    d = i
    i = i/100
    index_a = 0
    iii = 0
    for filename in glob.glob(path_old_folder+ '/*.' + file_type):
        img = logoim(filename, logo_file)

        index += 1
        index_a += 1
#        print(d,'/',index)
        progress(iii, index, d)
        if index_a >= i:
            iii += 1
            index_a = index_a - i


#        now = datetime.now()
#        current_time = now.strftime("%y-%m-%d-")
#        img.save(path_new_folder +'/img'+current_time+ str(index)+'.' +new_file_type)
        li = list(filename.split((b'\\').decode()))

        img.save(path_new_folder + '/' + str(li[1]))
    progress(100,d,d)

   # logoim(r'/' + 'sea.jpg')


if __name__ == '__main__':
    main()
