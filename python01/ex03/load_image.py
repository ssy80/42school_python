from matplotlib import image
from numpy import array
from PIL import Image
from os import path as ospath


def ft_load(path: str) -> array:
    """
    Load a JPG/JPEG image file and convert it to a array, and return the image array.
    """
    file_ext = ospath.splitext(path)[1][1:].upper()
    if not (file_ext == "JPG" or file_ext == "JPEG"):
        raise ValueError("file does not have extension as JPG or JPEG")

    try:
        with Image.open(path) as img:
            file_format = img.format
            if file_format != "JPEG":
                raise ValueError("actual file is not JPEG format")
    except Exception:
        raise ValueError("file not found or actual file is not JPEG format")

    img_arr = image.imread(path)
    print("The shape of image is:", img_arr.shape)
    return img_arr



"""def main():

    try:

        print(ft_load("landscape.jpg"))
        #print(ft_load("animal.jpeg"))

        #print(ft_load("notes.jpg"))
        #print(ft_load("androidparty.jpg"))


    except (ValueError, Exception) as e:
        print(f"Erorr: {e}")


if __name__ == "__main__":
    main()"""
