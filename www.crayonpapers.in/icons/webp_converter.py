from PIL import Image
import glob
import shutil
import os


def convert_to_webp(seperate=1, scale=0.5, quality=50):
    """Convert image to WebP.
    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    os.makedirs("webp", exist_ok=True)
    for x in glob.glob("*.*"):
        if "webp" in x:
            continue
        try:
            basename = x.split(".")[0]
            img = Image.open(x)
            width, height = img.size
            img = img.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
            newname = basename + ".webp"
            img.save(newname, format="webp", quality=quality)  # Convert image to webp
            if seperate:
                shutil.move(newname, "./webp/" + newname)
            print("saved", x)
        except Exception as e:
            print(e)
            # raise e


if __name__ == "__main__":
    convert_to_webp(seperate=0, scale=0.75, quality=80)
