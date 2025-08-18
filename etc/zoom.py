from matplotlib import image, pyplot as plt
from numpy import array, expand_dims
from PIL import Image
from os import path as ospath
from load_image import ft_load


def show_image(img_array):
    #img = mpimg.imread(path)
    plt.imshow(img_array)
    #plt.xlabel('X axis (pixels)')
    #plt.ylabel('Y axis (pixels)')
    #plt.title('Image with axis scale')
    #plt.grid(False)  # Optional: show grid lines if you want
    plt.show()


def zoom(img_array, col_left, col_right, row_upper, row_lower):

    height = img_array.shape[0]
    width = img_array.shape[1]

    if col_left > width or col_left < 0 or col_right > width or col_right < 0:
        raise ValueError(f"col_left, col_right must be between 0 and {width}")
    if row_upper > height or row_upper < 0 or row_lower > height or row_lower < 0:
        raise ValueError(f"row_upper, row_lower must be between 0 and {height}")
    
    
    #img_resized = Image.fromarray(img_array).resize((400, 400), Image.LANCZOS)
    #img_gray = Image.fromarray(img_array).convert("L").resize((400, 400), Image.LANCZOS)
    #img_gray = Image.fromarray(img_array).convert("L"), Image.LANCZOS)
    #img_gray = Image.fromarray(img_array).convert("L")#.resize(width,height), Image.LANCZOS)
    #img_gray = Image.fromarray(img_array).convert("L")
    #height = img_array.shape[0]
    #width = img_array.shape[1]

    #side = min(width, height)
    """left = (width - side) // 2
    upper = (height - side) // 2
    crop_box = (left, upper, left + side, upper + side)"""

    
    #img_array = array(img_gray)

    #left = 450
    #right = 850
    #upper = 100
    #lower = 500

    cropped_array = img_array[row_upper:row_lower, col_left:col_right, :]
    #cropped_array = array(img_gray)

    img = Image.fromarray(cropped_array)
    img_gray = img.convert("L")
    cropped_array = array(img_gray)

    #img_array = array(img_gray)
    #img_array = array(cropped_array)
    #print(f"New shape after slicing: {img_array.shape}")
    img_array = expand_dims(cropped_array, axis=-1)
    print(f"New shape after slicing: {img_array.shape}")
    return img_array
    #return cropped_array



def main():
    try:

        img_array = ft_load("animal.jpeg")
        print(img_array)

        col_left = 450
        col_right = 850
        row_upper = 100
        row_lower = 500

        img_array = zoom(img_array, col_left, col_right, row_upper, row_lower)
        print(img_array)
        show_image(img_array)
        
    except (ValueError, Exception) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
