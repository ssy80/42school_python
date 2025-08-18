import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from numpy import array


def show_image(img_array):
    """
    Display image from img_array
    """
    plt.imshow(img_array)
    plt.show()


def ft_invert(array) -> array:
    """
    Invert color of image
    """
    array = 255 - array
    return array


# 0 - red, 1 - green, 2 - blue
def ft_red(array) -> array:
    """
    Keep red channel, set green and blue channel of image to 0
    """
    array1 = array.copy()
    array1[:, :, 1] = 0
    array1[:, :, 2] = 0
    return array1


def ft_green(array) -> array:
    """
    Keep green channel, set red and blue channel of image to 0
    """
    array1 = array.copy()
    array1[:, :, 0] = 0
    array1[:, :, 2] = 0
    return array1


def ft_blue(array) -> array:
    """
    Keep blue channel, set red and green channel of image to 0
    """
    array1 = array.copy()
    array1[:, :, 0] = 0
    array1[:, :, 1] = 0
    return array1


# when all three channels (R, G, B) are set to the same value,
# the color is always a shade of grey
# gray = dot(array1[:,:,:3], [0.299, 0.587, 0.114])
# -> gray=(R×0.299)+(G×0.587)+(B×0.114)
# dot product / matrix multiplication
# np.dot works along the last dimension of the array (the 3 channels).
# np.dot does for every pixel in the image.
def ft_grey(array) -> array:
    """
    Multiply all pixels(R,G,B) with grey weights (0.299, 0.587, 0.114)
    to get grey values
    Set same grey values to (R,G,B) to change image to grey scale
    """
    array1 = array.copy()

    gray_weights = [0.299, 0.587, 0.114]
    gray = np.dot(array1[:, :, :3], gray_weights)
    gray = gray.astype(np.uint8)
    array1[:, :, 0] = gray
    array1[:, :, 1] = gray
    array1[:, :, 2] = gray
    return array1


def main():

    try:

        org_array = ft_load("landscape.jpg")
        print(org_array)

        img_array = ft_invert(org_array)
        show_image(img_array)

        img_array = ft_red(org_array)
        show_image(img_array)

        img_array = ft_green(org_array)
        show_image(img_array)

        img_array = ft_blue(org_array)
        show_image(img_array)

        img_array = ft_grey(org_array)
        show_image(img_array)

        print(ft_invert.__doc__)

    except (ValueError, Exception) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
