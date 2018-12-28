import os
import cv2

DEBUG = False
debug = lambda s : print(s) if DEBUG else None 

def compress(quality=3, directory="."):
    """
    Compress images within the working directory or directory.
    Quality can be a percentage or one of the following (lower percentage is lower quality and lower size):
    1. 80%
    2. 60%
    3. 40%
    4. 20%
    """
    quality_switch = {1:80,2:60,3:40,4:20}
    try:
        QUALITY = quality_switch[quality]
    except:
        if 0<=quality<=100:
            QUALITY = quality
        else:
            raise ValueError("Quality must be 1, 2, 3, 4, or a percentage.")
    
    os.chdir(directory)

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
