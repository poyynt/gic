import cv2
import os
import tkinter as tk
import tkinter.messagebox as tkmessagebox
import time


# For Debigging only, do not turn this on in operation
DEBUG = False
debug = lambda s : print(s) if DEBUG else None


window = tk.Tk()
window.title("GIC")

text0 = tk.Label(window, text="All images in this folder will be compressed with name \"compressed_originalfilename\"")
text0.pack()
text = tk.Label(window,text="Select Compression Level From 1 to 4 (4 is the lowest quality, lowest size)")
text.pack()

compression = tk.Scale(window, from_=1, to=4, orient=tk.HORIZONTAL)
compression.set(3)
compression.pack(anchor=tk.CENTER)


def read_compression_callback():
    global compression,read_compression,text,button_pressed,image_quality,window
    image_quality = compression.get()
    compression.destroy()
    read_compression.destroy()
    text["text"] = "Status: Compressing..."
    text['padx'] = 10
    text['pady'] = 10
    text.pack()
    time.sleep(1)
    compress()
    tkmessagebox.showinfo("Done","Done.")
    window.quit()
#    button_pressed = True
#    window.destroy()
#    return image_quality
def compress():
    global image_quality
    quality_switch = {1:80,2:60,3:40,4:20}
    QUALITY = quality_switch[image_quality]

    directory_list = os.listdir() # This should be here not to include newer files.

    # To Me from the Future:
    # cv2.IMWRITE_PNG_COMPRESSION is from 0 to 9 and the higher means better
    # compression, more time.
    # cv2.IMWRITE_JPEG_QUALITY is from 0 to 100 and the higher means better 
    # quality, bigger size and less time.
    # So, the PNG compression must be 9 and jpeg quality should be something 
    # about 80.

    compression_parameters = [cv2.IMWRITE_PNG_COMPRESSION, 9,cv2.IMWRITE_JPEG_QUALITY, QUALITY]

    for i in directory_list:
        if i.split(".")[-1].lower() != "png" and i.split(".")[-1].lower() != "jpg":
            continue # Do not do operations on non-images!
        if i.find("compressed_") != -1:
            continue # Do not do operations on previously compressed files
        img = cv2.imread(i)
        new_name = "compressed_" + i.split(".")[0] + "." + i.split(".")[-1].lower()
        debug(new_name)
        cv2.imwrite(new_name,img,compression_parameters)
        debug('finished')
        debug("Old: " + str(os.path.getsize(i)))
        debug("New: " + str(os.path.getsize(new_name)))


read_compression = tk.Button(window,text="Compress", command=read_compression_callback)
read_compression.pack()

def run():
    button_pressed = False
    image_quality = None

    window.mainloop()

