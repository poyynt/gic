import cv2
import os

# For Debigging only, do not turn this on in operation
DEBUG = False
debug = lambda s : print(s) if DEBUG else None

def compress(image_quality):
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

def run():
    image_quality = input("Enter a compression level (1-4, higher is lower size): ")
    while (not image_quality.isnumeric()) or image_quality not in ("1", "2", "3", "4"):
        image_quality = input("Bad input.\nEnter a compression level (1-4, higher is lower size): ")
    image_quality = int(image_quality)
    print("Compressing...", end="\r")
    compress(image_quality)
    print("Finished.      ")
