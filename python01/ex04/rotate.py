import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(img_array, col_left, col_right, row_upper, row_lower):
    """
    Cropped and return the image array, according to points given.
    """
    height = img_array.shape[0]
    width = img_array.shape[1]

    if col_left > width or col_left < 0 or col_right > width or col_right < 0:
        raise ValueError(f"col_left, col_right must be between 0 and {width}")
    if row_upper > height or row_upper < 0 or row_lower > height or row_lower < 0:
        raise ValueError(f"row_upper, row_lower must be between 0 and {height}")
    
    cropped_array = img_array[row_upper:row_lower, col_left:col_right, :]
    
    gray_array = np.dot(cropped_array[:, :, :3], [0.299, 0.587, 0.114])
    gray_array = gray_array.astype(np.uint8)

    return gray_array


def transpose(img_array):
    """
    Transpose (H, W) to (W, H)
    """
    height, width = img_array.shape
    img_rotated = np.zeros((width, height), dtype=img_array.dtype)

    for i in range(height):
        for j in range(width):
            img_rotated[j][i] = img_array[i][j]

    return img_rotated


def main():

    try:

        img_array = ft_load("animal.jpeg")

        col_left = 450
        col_right = 450 + 400
        row_upper = 100
        row_lower = 100 + 400

        img_array = zoom(img_array, col_left, col_right, row_upper, row_lower)
        print("The shape of image is:", img_array.shape)
        print(img_array)

        img_array = transpose(img_array)
        print(f"New shape after Transpose: {img_array.shape}")
        print(img_array)

        plt.imshow(img_array, cmap="gray")
        plt.show()

    except (ValueError, Exception) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
