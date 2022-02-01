# Credits: NIKHIL SWAMI
# USAGE
# KEEP ALL FILES IN FOLDER ALONG WITH THIS CODE.
# CODE IS SELF EXPLANATORY THOUGH

import os
from PIL import Image
import multiprocessing


def custom_resize(sizetupleXY, factor=0.8):
    x, y = sizetupleXY
    x = int(x * factor)
    y = int(y * factor)
    # if
    return (x, y)


def compress_file(imgpath, format="webp", factor=0.5, quality=80):
    """
    Atomic file compression function for multiprocessing Processes,
    allows us to apply this function to image path and the result is put in
    "./compressed" folder created adjacent
    """
    try:
        print(imgpath)
        size = os.path.getsize(imgpath)
        currentImg = Image.open(imgpath).convert("RGBA")
        currentImg = currentImg.resize(custom_resize(currentImg.size, factor=factor))
        savingName = imgpath.split(".")[0] + "." + format
        currentImg = currentImg.save(
            f"./compressed/{savingName}", quality=quality, optimize=True, format=format
            )
        sizeDifference = size - os.path.getsize(f"./compressed/{savingName}")

        pass
    except Exception as e:
        open("errors.log", "a").write(str(e) + "\n")
        open("errors.log", "a").write(str(e) + "\n")
    finally:
        os.replace(imgpath, "orignal/" + imgpath)


def get_images():
    return [
        x
        for x in os.listdir()
        if x.endswith("png")
        or x.endswith("jpg")
        or x.endswith("jpeg")
        or x.endswith("webp")
        ][:]


# -----------------------------------------
try:
    # WORKING_DIR='C:\\Users\\dell\\Downloads\\PicturesJAN2020\\Screenshots 2019'
    # os.chdir(WORKING_DIR)
    ...
except Exception as e:
    print(e)
finally:
    if not os.path.exists("compressed"):
        os.makedirs("compressed")
    if not os.path.exists("orignal"):
        os.makedirs("orignal")
# -----------------------------------------

if __name__ == "__main__":
    """
    Change the folder to your target folder where
    the images which need to be compressed are present
    # open('000tempfile','w').write('')
    """
    POOL = multiprocessing.Pool(6)
    savings = multiprocessing.Manager().Value("i", 0, lock=True)

    result = [
        POOL.apply_async(compress_file, (file,), {"quality": 100, "factor": 0.20})
        for file in get_images()
        ]
    [x.get() for x in result]

    # ------------------TESTING--------------------
    # singleThead=[compress_file(x,savings) for x in get_images()]
