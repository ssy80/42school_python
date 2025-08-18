import numpy as np


def is_2d_list(lst):
    """
    Check is valid list, return False if not.
    length must not be empty, must be a list instance, every list in the main list is also a list,
    all inner list must not be empty
    """
    if not isinstance(lst, list):
        return False

    if len(lst) == 0:
        return False

    if not all(isinstance(x, list) for x in lst):
        return False

    if any(len(x)==0 for x in lst):
        return False

    first = len(lst[0])
    if not all(len(x)==first for x in lst):
        return False

    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    Display shape of current list and shape after slicing with start and end.
    """
    if not is_2d_list(family):
        raise ValueError("not a list of list, or not list of list with equal length, or empty list")

    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    arr = arr[start:end]
    print(f"My new shape is : {arr.shape}")
    arr = arr.tolist()
    return arr



"""def main():

    family = [[1.80, 78.4,],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]]
    #family = [[],[],[]]

    try:

        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

    except (ValueError, Exception) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()"""
